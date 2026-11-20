@echo off
chcp 65001 >nul
title Step 4: Backup 6 Months (Samsung Only)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8

echo ============================================
echo   STEP 4 (OPTIONAL): BACKUP +6 MONTHS (Samsung)
echo   Applies only to eligible Samsung devices
echo ============================================
echo.
python ultra0.py --account "current@device" --no-add --force --stack --plan pro6c
echo.
pause
