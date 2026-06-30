@echo off
setlocal enabledelayedexpansion

echo [INFO] Starting build process with uv

:: ------------------------------------------------------------
:: 1. Configuration
:: ------------------------------------------------------------
set VENV_DIR=.venv
set SPEC_FILE=build.spec
set DIST_DIR=dist
set SRC_DIR=src

:: ------------------------------------------------------------
:: 2. Check for uv
:: ------------------------------------------------------------
where uv >nul 2>nul
if errorlevel 1 (
    echo [ERROR] uv is not installed or not in PATH.
    exit /b 1
)

:: ------------------------------------------------------------
:: 3. Create virtual environment with uv
:: ------------------------------------------------------------
if not exist %VENV_DIR% (
    echo [INFO] Creating virtual environment with uv in %VENV_DIR%
    uv venv %VENV_DIR%
) else (
    echo [INFO] Virtual environment already exists.
)

echo [INFO] Activating virtual environment
call %VENV_DIR%\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment.
    exit /b 1
)

:: ------------------------------------------------------------
:: 4. Sync dependencies from pyproject.toml and uv.lock
:: ------------------------------------------------------------
echo [INFO] Syncing dependencies with uv
uv sync
if errorlevel 1 (
    echo [ERROR] Failed to sync dependencies.
    exit /b 1
)

:: Ensure pyinstaller is available (install if missing)
where pyinstaller >nul 2>nul
if errorlevel 1 (
    echo [INFO] pyinstaller not found, installing with uv
    uv pip install pyinstaller
)

:: ------------------------------------------------------------
:: 5. Clean old dist
:: ------------------------------------------------------------
if exist %DIST_DIR% (
    echo [INFO] Removing old dist directory
    rmdir /s /q %DIST_DIR%
)

:: ------------------------------------------------------------
:: 6. Run PyInstaller
:: ------------------------------------------------------------
echo [INFO] Running PyInstaller with spec file %SPEC_FILE%
pyinstaller %SPEC_FILE%
if errorlevel 1 (
    echo [ERROR] PyInstaller build failed.
    exit /b 1
)

:: ------------------------------------------------------------
:: 7. Copy external resources
:: ------------------------------------------------------------
echo [INFO] Copying external files from %SRC_DIR% to %DIST_DIR%...

if exist %SRC_DIR%\icon.png (
    copy %SRC_DIR%\icon.png %DIST_DIR%\
    echo [INFO] icon.png copied
) else (
    echo [ERROR] icon.png not found in %SRC_DIR%.
)

if exist README.md (
    copy README.md %DIST_DIR%\
    echo [INFO] README.md copied
) else (
    echo [ERROR] README.md not found in %SRC_DIR%.
)

if exist LICENSE (
    copy LICENSE %DIST_DIR%\
    echo [INFO] LICENSE copied
) else (
    [ERROR] LICENCE not found in %SRC_DIR%.
)

:: ------------------------------------------------------------
:: 8. Finish
:: ------------------------------------------------------------
echo [INFO] Build completed successfully.
echo [INFO] Output is in %DIST_DIR%\NitroSensualEnhanced.exe
exit /b 0
