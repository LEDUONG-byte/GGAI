@echo off
chcp 65001 >nul
title Step 1: Activate 12-Month Free Trial
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8

echo ============================================
echo   STEP 1: GOOGLE AI PRO (5 TB) - 12 MONTHS FREE
echo ============================================
echo.
python ultra0.py --account "current@device" --no-add --force --plan pro12
echo.
pause
