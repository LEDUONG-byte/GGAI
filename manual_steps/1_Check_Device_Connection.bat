@echo off
chcp 65001 >nul
title Check Device Connection & Frida
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8

echo ============================================
echo   Check ADB / Frida / Billing Module
echo ============================================
echo.
python ultra0.py --check
echo.
pause
