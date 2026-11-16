# The BERIL wiki as served on SPIN (beril.kbase.us/wiki): the built site plus
# the small server in src/beril_wiki/serve.py.
#
# Two ways to get the site into the image, chosen by the build arg SITE_FROM:
#
#   hostsite (default)  the site was built on the host first, as CI does:
#                         WIKI_BASE_URL=localhost:8080/wiki scripts/build_quartz.sh
#                         docker build -t beril-wiki .
#   site                the site is built inside the image (node + uv + a Quartz
#                       clone, so it needs network and takes a few minutes), which
#                       is what the observatory's docker-compose wiki service uses:
#                         docker build --build-arg SITE_FROM=site \
#                           --build-arg WIKI_BASE_URL=localhost:8000/wiki -t beril-wiki .
#                       Without the repo's .git the search vectors cannot be pulled
#                       from the history branch; the build warns and meaning search
#                       is empty until an artifact with vectors is loaded.
#
# The baked site (/srv/site) and corpus (/srv/corpus) are the fallback. With
# WIKI_ARTIFACT_* set (see README, "Run the image locally") the server fetches
# the current site artifact into WIKI_SITE_ROOT on start and on
# POST /wiki/_admin/reload, so content changes need no new image. Mount a
# volume at /srv/artifacts to keep the unpacked artifact across restarts.
ARG SITE_FROM=hostsite

# --- hostsite: the site as built on the host --------------------------------
FROM scratch AS hostsite
COPY quartz/public/ /site/
COPY quartz/corpus/ /corpus/

# --- site: build the site inside the image ----------------------------------
FROM node:22-bookworm-slim AS site
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:0.12.20 /uv /uvx /usr/local/bin/
ENV UV_PYTHON_INSTALL_DIR=/opt/uv-python UV_LINK_MODE=copy UV_COMPILE_BYTECODE=0
WORKDIR /build
COPY pyproject.toml uv.lock ./
RUN uv python install 3.12 && uv sync --frozen --no-dev --no-install-project
COPY src ./src
COPY theme ./theme
COPY scripts ./scripts
COPY contract ./contract
COPY state ./state
COPY wiki ./wiki
# A local vector store, when the host has one (gitignored; absent in CI).
COPY searc[h]/ ./search/
RUN uv sync --frozen --no-dev
ARG WIKI_BASE_URL=localhost:8000/wiki
RUN WIKI_BASE_URL="$WIKI_BASE_URL" WIKI_SKIP_GATES=1 scripts/build_quartz.sh \
    && mkdir -p /site /corpus \
    && cp -R quartz/public/. /site/ && cp -R quartz/corpus/. /corpus/

# --- runtime -----------------------------------------------------------------
FROM ghcr.io/astral-sh/uv:0.12.20-python3.12-trixie-slim
ARG SITE_FROM

# SPIN runs the pod as this uid/gid, the same account the observatory image uses.
RUN addgroup --system --gid 76761 beril_app && \
    adduser --system --uid 76761 --home /home/beril --ingroup beril_app beril

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    PYTHONPATH=/app \
    WIKI_SITE_DIR=/srv/site \
    WIKI_CORPUS_DIR=/srv/corpus \
    WIKI_SITE_ROOT=/srv/artifacts \
    WIKI_PREFIX=/wiki

# Only the server's dependencies (the `serve` group), exactly as uv.lock pins them.
COPY pyproject.toml uv.lock /tmp/build/
RUN uv export --project /tmp/build --frozen --only-group serve --no-emit-project \
        -o /tmp/build/requirements.txt && \
    uv pip install --system --require-hashes -r /tmp/build/requirements.txt && \
    rm -rf /tmp/build

# serve.py and the two modules it imports; nothing else from the package.
COPY src/beril_wiki/__init__.py src/beril_wiki/serve.py src/beril_wiki/wiki_api.py \
     /app/beril_wiki/
COPY src/beril_wiki/publish/__init__.py src/beril_wiki/publish/artifact.py \
     /app/beril_wiki/publish/
COPY --from=${SITE_FROM} /site/ /srv/site/
COPY --from=${SITE_FROM} /corpus/ /srv/corpus/
RUN mkdir -p /srv/artifacts && chown beril:beril_app /srv/artifacts

USER beril
EXPOSE 8080

ARG GIT_COMMIT
ENV BERIL_WIKI_GIT_COMMIT=${GIT_COMMIT}

CMD ["uvicorn", "beril_wiki.serve:app", "--host", "0.0.0.0", "--port", "8080", \
     "--proxy-headers", "--forwarded-allow-ips=*", "--no-server-header"]
