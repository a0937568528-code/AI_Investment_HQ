@echo off
cd /d "%~dp0"

echo ==========================================
echo AI Investment HQ - TWII DATA UPDATE
echo ==========================================
echo.

python update_tw.py

if errorlevel 1 (
    echo.
    echo UPDATE FAILED.
    pause
    exit /b 1
)

echo.
echo UPDATE COMPLETE.
echo TWII DATA UPDATED.
echo NO GAP CALCULATION.
echo NO RISK CONTROL CALCULATION.
echo.
pause
