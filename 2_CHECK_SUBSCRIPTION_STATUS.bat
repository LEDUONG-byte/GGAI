@echo off
chcp 65001 >nul
title Check Google AI Pro Subscription Status
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

echo ========================================================
echo   CHECK GOOGLE ONE / GOOGLE AI SUBSCRIPTION STATUS
echo ========================================================
echo.
python ultra0.py --status
echo.
pause
