@echo off
cd /d "%~dp0"
echo Installing dependencies...
py -3 -m pip install -r requirements.txt
echo Starting chart at http://127.0.0.1:8000
start "" http://127.0.0.1:8000
py -3 -m mkr_sky serve --host 127.0.0.1 --port 8000
pause
