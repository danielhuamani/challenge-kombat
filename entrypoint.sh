#!/usr/bin/env bash
echo "Starting docker entrypoint"

uvicorn main:app --reload --host 0.0.0.0 --port 8000