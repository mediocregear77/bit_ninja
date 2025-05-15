#!/bin/bash
# server/launch.sh
# Launches the Bitcoin_Ninja Flask API server

echo "[*] Starting Bitcoin_Ninja GPU Flask Server..."

# Ensure Python uses UTF-8
export PYTHONIOENCODING=utf8
export FLASK_APP=flask_server.py
export FLASK_ENV=production

# Change to server directory and launch
cd "$(dirname "$0")"
python3 flask_server.py
