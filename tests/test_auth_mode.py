"""BERIL_WIKI_AUTH picks how jobs authenticate; nothing about caching depends on it."""

from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from beril_wiki.agentic import codex as C
from beril_wiki.agentic import runtime as R

KEY, URL = "ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL"
OKEY, OURL = "OPENAI_API_KEY", "OPENAI_BASE_URL"


@pytest.fixture
def creds(monkeypatch):
    monkeypatch.setenv(KEY, "sk-test")
    monkeypatch.setenv(URL, "https://api.cborg.lbl.gov")
    monkeypatch.setenv("CLAUDE_CODE_OAUTH_TOKEN", "oauth-must-go")
    monkeypatch.setenv("CLAUDE_CODE_USE_BEDROCK", "1")
    monkeypatch.setenv(OKEY, "sk-openai")
    monkeypatch.setenv(OURL, "https://api.cborg.lbl.gov")
    monkeypatch.setenv("OPENAI_ORG_ID", "org-must-go")
    monkeypatch.setenv("CODEX_HOME", "/nonexistent")


def test_default_mode_is_subscription_and_strips_everything(creds, monkeypatch):
    monkeypatch.delenv("BERIL_WIKI_AUTH", raising=False)
    assert R.auth_mode() == "subscription"
    env = R.job_env(1000)
    assert all(env[k] == "" for k in R.AUTH_ENV)
    assert env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] == "1000"
    assert R.stripped_env() == R.AUTH_ENV
    assert R.credential_expected("none") and not R.credential_expected(KEY)
    session = C.session_env()
    assert not any(k.startswith(C.ENV_PREFIXES) for k in session)
    assert C.overrides()[0] == 'forced_login_method="chatgpt"'
    assert C.overrides()[1:] == C.OVERRIDES[1:]


def test_api_mode_passes_only_the_keys_through(creds, monkeypatch):
    monkeypatch.setenv("BERIL_WIKI_AUTH", "api")
    assert R.auth_mode() == "api"
    env = R.job_env()
    assert env[KEY] == "sk-test" and env[URL] == "https://api.cborg.lbl.gov"
    assert env["CLAUDE_CODE_OAUTH_TOKEN"] == "" and env["CLAUDE_CODE_USE_BEDROCK"] == ""
    assert set(R.stripped_env()) == set(R.AUTH_ENV) - set(R.API_ENV)
    assert R.credential_expected(KEY) and not R.credential_expected("none")
    session = C.session_env()
    assert session[OKEY] == "sk-openai" and session[OURL] == "https://api.cborg.lbl.gov"
    assert "OPENAI_ORG_ID" not in session and KEY not in session
    assert C.overrides()[0] == 'forced_login_method="api"'


def test_api_mode_without_a_key_is_refused_before_any_job(creds, monkeypatch):
    monkeypatch.setenv("BERIL_WIKI_AUTH", "api")
    monkeypatch.setattr(R.subprocess, "run", lambda *a, **k: pytest.fail("no CLI call in api mode"))
    R.check_auth("claude")
    monkeypatch.delenv(KEY)
    with pytest.raises(R.WorkflowError, match="needs ANTHROPIC_API_KEY"):
        R.check_auth("claude")
    monkeypatch.setenv("BERIL_WIKI_AUTH", "nope")
    with pytest.raises(R.WorkflowError, match="BERIL_WIKI_AUTH"):
        R.auth_mode()


def test_subscription_mode_still_verifies_the_login(creds, monkeypatch):
    monkeypatch.delenv("BERIL_WIKI_AUTH", raising=False)
    seen = {}

    def auth_run(*args, **kwargs):
        seen["env"] = kwargs["env"]
        return SimpleNamespace(returncode=0, stdout=json.dumps({"loggedIn": False}))

    monkeypatch.setattr(R.subprocess, "run", auth_run)
    with pytest.raises(R.WorkflowError, match="subscription login is required"):
        R.check_auth("claude")
    assert seen["env"][KEY] == ""


def account_of(kind):
    account = None if kind is None else SimpleNamespace(root=SimpleNamespace(type=kind))
    return SimpleNamespace(account=lambda: SimpleNamespace(account=account))


def test_codex_auth_follows_the_mode(creds, monkeypatch):
    monkeypatch.setenv("BERIL_WIKI_AUTH", "api")
    C.check_auth(account_of("apiKey"))
    with pytest.raises(R.WorkflowError, match="did not take OPENAI_API_KEY"):
        C.check_auth(account_of("chatgpt"))
    monkeypatch.delenv("BERIL_WIKI_AUTH")
    C.check_auth(account_of("chatgpt"))
    with pytest.raises(R.WorkflowError, match="ChatGPT"):
        C.check_auth(account_of("apiKey"))


def test_codex_home_links_the_login_only_in_subscription_mode(creds, tmp_path, monkeypatch):
    monkeypatch.setenv("BERIL_WIKI_AUTH", "api")
    home = C.prepare_home(tmp_path / "store", "a")
    assert not (home / "auth.json").is_symlink() and not (home / "auth.json").exists()
    monkeypatch.delenv("BERIL_WIKI_AUTH")
    home = C.prepare_home(tmp_path / "store", "a")
    assert (home / "auth.json").is_symlink()


def test_stage_subprocess_env_follows_the_mode(creds, tmp_path, monkeypatch):
    from beril_wiki.agentic import runner

    seen = {}

    class Done:
        pid = 1
        returncode = 0

        def poll(self):
            return 0

    def popen(command, **kwargs):
        seen["env"] = kwargs["env"]
        return Done()

    monkeypatch.setattr(runner.subprocess, "Popen", popen)
    config = tmp_path / "config.json"
    config.write_text("{}")
    (tmp_path / "work").mkdir()
    monkeypatch.delenv("BERIL_WIKI_AUTH", raising=False)
    runner.run_stage(tmp_path / "work", config, "x", "stages.fetch", [])
    assert not any(k in seen["env"] for k in R.AUTH_ENV)
    assert OKEY in seen["env"]  # Codex strips its own prefixes inside the stage
    monkeypatch.setenv("BERIL_WIKI_AUTH", "api")
    runner.run_stage(tmp_path / "work", config, "x", "stages.fetch", [])
    assert seen["env"][KEY] == "sk-test" and seen["env"][URL] == "https://api.cborg.lbl.gov"
    assert "CLAUDE_CODE_OAUTH_TOKEN" not in seen["env"]
    assert seen["env"]["BERIL_WIKI_AUTH"] == "api"
