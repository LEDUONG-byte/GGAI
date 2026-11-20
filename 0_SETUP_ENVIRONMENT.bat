@echo off
chcp 65001 >nul
title Automated Environment Setup
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

echo ============================================================
echo   AUTOMATED ENVIRONMENT SETUP & DIAGNOSTICS
echo   - Verify Python version (3.10+)
echo   - Install & configure Frida 16.5.9
echo   - Detect or download Android Debug Bridge (ADB)
echo   - Connect to Android device / emulator and run self-test
echo ============================================================
echo.
pause

python setup_env.py

echo.
echo ------------------------------------------------------------
echo   Done! If all checks passed, launch:
echo   "1_AUTO_STACK_24_MONTHS.bat" to start.
echo ------------------------------------------------------------
pause
