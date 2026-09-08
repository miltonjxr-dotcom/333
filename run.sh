#!/bin/sh
cd "$(dirname "$0")"
python3 -m pip install -r requirements.txt
echo "Opening http://127.0.0.1:8000"
(sleep 1; python3 -m webbrowser http://127.0.0.1:8000) >/dev/null 2>&1 &
exec python3 -m mkr_sky serve --host 127.0.0.1 --port 8000
