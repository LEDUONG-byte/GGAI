@echo off
chcp 65001 >nul
title Step 3: Stack 6 Months (Total: 24 Months)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8

echo ============================================
echo   STEP 3: EXTEND +6 MONTHS (TOTAL: 24 MONTHS)
echo   (Run only after Step 2 has completed)
echo ============================================
echo.
python ultra0.py --account "current@device" --no-add --force --stack --plan pro6c
echo.
pause
