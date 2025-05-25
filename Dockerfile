FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /install

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --prefix=/install/local -r requirements.txt

FROM debian:bookworm-slim AS runtime

LABEL org.opencontainers.image.authors="Matthew Lozinski <matthewlozinski@gmail.com>"
LABEL org.opencontainers.image.title="Weather Application"
LABEL org.opencontainers.image.description="Service to query weather data and to log"
LABEL org.opencontainers.image.version="1.0.0"

ENV PORT=8080
ENV PATH="/opt/local/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt
COPY --from=builder /install/local /opt/local
COPY app /opt/app
COPY entrypoint.sh /opt/entrypoint.sh

RUN chmod +x /opt/entrypoint.sh

EXPOSE 8080

HEALTHCHECK --interval=50s --timeout=5s --start-period=8s --retries=8 \
  CMD curl -f http://localhost:8080 || exit 1

ENTRYPOINT ["/opt/entrypoint.sh"]
