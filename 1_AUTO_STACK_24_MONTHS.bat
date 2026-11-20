@echo off
chcp 65001 >nul
title Automated 24-Month Google AI Pro Stacking
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

echo ========================================================
echo   AUTOMATED 24-MONTH GOOGLE AI PRO (5 TB) STACKING
echo   Sequence: 12 Months -> 18 Months -> 24 Months
echo ========================================================
echo.
python ultra0.py --account "current@device" --no-add --force --auto-stack
echo.
pause
