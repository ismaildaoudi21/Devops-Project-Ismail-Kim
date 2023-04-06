#!/bin/sh

# Start Redis in the background
redis-server --daemonize yes

cd /app
exec python3 run.py
