# The BERIL wiki as served on SPIN (beril.kbase.us/wiki): the built site plus
# the small server in src/beril_wiki/serve.py. The site is NOT built here: build
# it first, for the URL it will be served at, then build the image.
#
#   WIKI_BASE_URL=localhost:8080/wiki scripts/build_quartz.sh
#   docker build -t beril-wiki .
#   docker run --rm -p 8080:8080 beril-wiki     # http://localhost:8080/wiki/
#
# Building in the image would need the repo's .git (the search vectors come
# from the search-data branch) and network for the Quartz clone; CI already has
# both on the runner (.github/workflows/image.yml).
FROM ghcr.io/astral-sh/uv:0.12.20-python3.12-trixie-slim

# SPIN runs the pod as this uid/gid, the same account the observatory image uses.
RUN addgroup --system --gid 76761 beril_app && \
    adduser --system --uid 76761 --home /home/beril --ingroup beril_app beril

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    PYTHONPATH=/app \
    WIKI_SITE_DIR=/srv/site \
    WIKI_PREFIX=/wiki

# Only the server's dependencies (the `serve` group), exactly as uv.lock pins them.
COPY pyproject.toml uv.lock /tmp/build/
RUN uv export --project /tmp/build --frozen --only-group serve --no-emit-project \
        -o /tmp/build/requirements.txt && \
    uv pip install --system --require-hashes -r /tmp/build/requirements.txt && \
    rm -rf /tmp/build

COPY src/beril_wiki/__init__.py src/beril_wiki/serve.py /app/beril_wiki/
COPY quartz/public/ /srv/site/

USER beril
EXPOSE 8080

ARG GIT_COMMIT
ENV BERIL_WIKI_GIT_COMMIT=${GIT_COMMIT}

CMD ["uvicorn", "beril_wiki.serve:app", "--host", "0.0.0.0", "--port", "8080", \
     "--proxy-headers", "--forwarded-allow-ips=*", "--no-server-header"]
