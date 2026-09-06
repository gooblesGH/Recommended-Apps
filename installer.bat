@echo off
:: Prevents the window from closing instantly if there is an error
setlocal enabledelayedexpansion

echo ===================================================
echo   Installing Python Dependencies...
echo ===================================================
echo.

:: Check if Python is installed and accessible in the system PATH
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to your system PATH.
    echo Please install Python and check "Add Python to PATH" during setup.
    echo.
    pause
    exit /b
)

:: Upgrade pip to the latest version to avoid installation issues
echo [+] Upgrading pip...
python -m pip install --upgrade pip
echo.

:: Check if requirements.txt exists before trying to install
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt file not found in this folder.
    echo Please ensure requirements.txt is in the same directory as this batch file.
    echo.
    pause
    exit /b
)

:: Install the dependencies
echo [+] Installing required packages from requirements.txt...
python -m pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ===================================================
    echo   [SUCCESS] All dependencies installed successfully!
    echo ===================================================
) else (
    echo.
    echo [ERROR] Some packages failed to install. Please check the errors above.
)

echo.
pause
