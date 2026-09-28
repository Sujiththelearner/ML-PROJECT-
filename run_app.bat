@echo off
title Skill Gap Analyzer - Launcher
echo ============================================================
echo           STARTING SKILL GAP ANALYZER WEB PLATFORM          
echo ============================================================
echo.
echo Activating virtual environment and starting Streamlit...
echo (Keep this window open while using the application)
echo.

cd /d "%~dp0"
call "Skill-Gap-Analyzer\venv\Scripts\activate.bat"
"Skill-Gap-Analyzer\venv\Scripts\streamlit.exe" run app\app.py

pause
