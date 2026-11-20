@echo off
chcp 65001 >nul
title List Available Google AI Pro Offers
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8

echo ============================================
echo   List Free Trial Offers (Safe / Read-only)
echo ============================================
echo.
python ultra0.py --account "current@device" --no-add --force --list --plan pro12
echo.
pause
