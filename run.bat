@echo off
setlocal

:: Define paths
set PYTHON_PATH_FILE=vendor\python_path.txt

:: Check if the portable Python path is saved
if exist "%PYTHON_PATH_FILE%" (
    timeout 1
    :: Directly read the first line of the file
    set "PYTHON_EXEC="
    for /f "delims=" %%a in ('type "%PYTHON_PATH_FILE%"') do (
        set "PYTHON_EXEC=%%a"
        goto check_path
    )
    goto no_path_read
) else (
    echo [X] %PYTHON_PATH_FILE% not found.
    goto no_python_found
)

:check_path
echo [*] Python path [Using]: "%PYTHON_EXEC%"
timeout 1
:: Check if the Python executable exists
if exist "%PYTHON_EXEC%" (
    echo [**********************************************]
    echo [************* APPLICATION STARTING ***********]
    echo [**********************************************]
    timeout 1
    "%PYTHON_EXEC%" public\main.py
    exit /b
) else (
    echo [X] Python executable not found at: "%PYTHON_EXEC%"
    goto no_python_found
)
goto :eof

:no_path_read
echo [X] Could not read any line from "%PYTHON_PATH_FILE%".
goto no_python_found

:no_python_found
:: No valid Python found, calling setup script
echo No registered Python found, running python_resolver setup...
call Pyavel\python_resolver.bat
exit /b

:eof
endlocal