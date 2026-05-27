FROM nginx:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY templates/default.conf.template /etc/nginx/templates/default.conf.template
