@echo off
chcp 65001 >nul
title Step 2: Stack 6 Months (Total: 18 Months)
cd /d "%~dp0\.."
set PYTHONIOENCODING=utf-8

echo ============================================
echo   STEP 2: EXTEND +6 MONTHS (TOTAL: 18 MONTHS)
echo   (Run only after Step 1 has completed)
echo ============================================
echo.
python ultra0.py --account "current@device" --no-add --force --stack --plan pro6
echo.
pause
