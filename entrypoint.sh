#!/bin/sh
echo "[INFO] Start date: $(date)"
echo "[INFO] Author: Matthew Lozinski"
echo "[INFO] Listening on port: ${PORT:-8080}"

exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}
