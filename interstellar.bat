@echo off
title PROYECTO INTERSTELLAR - CSLG
echo Descargando Interstellar desde GitHub...
powershell -Command "Invoke-WebRequest -Uri https://raw.githubusercontent.com/kattiamenamartines-rgb/Interstellar-CSLG/main/main.py -OutFile main.py"
python main.py
pause
