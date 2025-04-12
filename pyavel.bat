@echo off
setlocal EnableDelayedExpansion

:: ───── Step 1: Check for global Python via Windows PATH ─────
powershell -Command "& { $pythonPath=(Get-Command python | Select-Object -ExpandProperty Source); Write-Host $pythonPath }" > temp_python_path.txt
set /p PYTHON_GLOBAL_PATH=<temp_python_path.txt
del temp_python_path.txt

if not "%PYTHON_GLOBAL_PATH%"=="" (
    powershell -Command "Write-Host '[*] Global Python detected at: %PYTHON_GLOBAL_PATH%' -ForegroundColor Yellow"

    :: Prompt user for next action
    powershell -Command "Write-Host 'Choose an option:' -ForegroundColor Cyan"
    echo [1] Copy global Python to portable vendor/
    echo [2] Download fresh portable Python to vendor/
    echo [3] Use global Python directly
    set /p choice="Enter your choice (1/2/3): "

    if "!choice!"=="1" (
    :: Get parent folder of python.exe path
    for %%F in ("%PYTHON_GLOBAL_PATH%") do set "PYTHON_DIR=%%~dpF"

    powershell -Command "Write-Host '[*] Copying global Python from: !PYTHON_DIR!' -ForegroundColor Yellow"
    xcopy /E /H /C /I "!PYTHON_DIR!\*" "vendor\python\"

    call :register_python_path vendor\python\python.exe
    powershell -Command "Write-Host '[OK] Global Python copied and registered as portable.' -ForegroundColor Green"
    exit /b
)else if "!choice!"=="2" (
        call :download_and_extract_python
        exit /b
    ) else if "!choice!"=="3" (
        powershell -Command "Write-Host '[OK] Using global Python directly.' -ForegroundColor Green"
        call :register_python_path %PYTHON_GLOBAL_PATH%
        exit /b
    ) else (
        powershell -Command "Write-Host '[X] Invalid option! Please restart and try again.' -ForegroundColor Red"
        pause
        exit /b
    )
)

:: ───── Step 2: Check if registered portable Python path exists ─────
if exist vendor\portable_python_path.txt (
    set /p portable_python_path=<vendor\portable_python_path.txt
    if exist "!portable_python_path!" (
        powershell -Command "Write-Host '[OK] Using registered portable Python: !portable_python_path!' -ForegroundColor Green"
        "!portable_python_path!"
        exit /b
    )
)

:: ───── Step 3: Check vendor fallback ─────
if exist vendor\python\python.exe (
    powershell -Command "Write-Host '[OK] Using vendor\python\python.exe' -ForegroundColor Green"
    call :register_python_path vendor\python\python.exe
    vendor\python\python.exe
    exit /b
)

:: ───── Step 4: Offer to install Python ─────
powershell -Command "Write-Host '[!] Python not found. Install now? (Y/N)' -ForegroundColor Red"
set /p install_choice="Your choice: "

if /I "%install_choice%"=="N" (
    powershell -Command "Write-Host '[X] Python is required to run this framework.' -ForegroundColor Red"
    pause
    exit /b
)

powershell -Command "Write-Host 'Install Python as Global or Portable? (G/P)' -ForegroundColor Cyan"
set /p install_type="Your choice: "

if /I "%install_type%"=="G" (
    powershell -Command "Write-Host '[*] Installing Python globally...' -ForegroundColor Yellow"
    powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = 'TLS12'; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe' -OutFile 'python_installer.exe'}"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    powershell -Command "Write-Host '[OK] Global Python installed.' -ForegroundColor Green"

    powershell -Command "& { $pythonPath=(Get-Command python | Select-Object -ExpandProperty Source); Write-Host $pythonPath }" > temp_python_path.txt
    set /p PYTHON_GLOBAL_PATH=<temp_python_path.txt
    del temp_python_path.txt

    if not "%PYTHON_GLOBAL_PATH%"=="" (
        call :register_python_path %PYTHON_GLOBAL_PATH%
        powershell -Command "Write-Host '[OK] Registered global Python.' -ForegroundColor Green"
        exit /b
    ) else (
        powershell -Command "Write-Host '[X] Failed to register global Python.' -ForegroundColor Red"
        pause
        exit /b
    )
) else if /I "%install_type%"=="P" (
    call :download_and_extract_python
    exit /b
)

powershell -Command "Write-Host '[X] Unexpected error. Exiting.' -ForegroundColor Red"
pause
exit /b

:: ────────────────────────────────────────────────────────────────
:: FUNCTIONS SECTION — must be at bottom
:: ────────────────────────────────────────────────────────────────

:register_python_path
if not exist vendor\python\ (
    mkdir vendor\python
)
if not exist vendor\portable_python_path.txt (
    echo Creating portable Python path registry...
    echo. > vendor\portable_python_path.txt
)
echo %1 > vendor\portable_python_path.txt
exit /b

:download_and_extract_python
set "PYTHON_ZIP=python-3.12.0-embed-amd64.zip"

echo [*] Downloading Portable Python...
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = 'TLS12'; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-amd64.zip' -OutFile '%PYTHON_ZIP%'; Write-Host '[OK] Download complete!' -ForegroundColor Green}"

echo [*] Extracting Portable Python...
powershell -Command "& {Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath 'vendor\python' -Force; Write-Host '[OK] Extraction complete!' -ForegroundColor Green}"
del "%PYTHON_ZIP%"

if not exist vendor\python\python.exe (
    powershell -Command "Write-Host '[X] Portable Python installation failed!' -ForegroundColor Red"
    pause
    exit /b
)

powershell -Command "Write-Host '[OK] Portable Python installed successfully.' -ForegroundColor Green"
call :register_python_path vendor\python\python.exe
exit /b

