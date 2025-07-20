@echo off
setlocal enabledelayedexpansion

:: Rutas fijas basadas en la instalación de Python
set PYTHON_ROOT=C:\Python313
set TCL_ROOT=%PYTHON_ROOT%\tcl

:: Verificar que existen los directorios necesarios
if not exist "%TCL_ROOT%\tcl8.6" (
    echo No se encontró el directorio de Tcl en: %TCL_ROOT%\tcl8.6
    pause
    exit /b 1
)

if not exist "%TCL_ROOT%\tk8.6" (
    echo No se encontró el directorio de Tk en: %TCL_ROOT%\tk8.6
    pause
    exit /b 1
)

:: Construir el comando de PyInstaller
set COMMAND=python -m PyInstaller ^
    --name="Organizador" ^
    --onefile ^
    --windowed ^
    --add-data "%TCL_ROOT%\tcl8.6;tcl\tcl8.6" ^
    --add-data "%TCL_ROOT%\tk8.6;tcl\tk8.6" ^
    --hidden-import="tkinter" ^
    --hidden-import="tkinter.filedialog" ^
    main.py

echo Ejecutando: %COMMAND%
%COMMAND%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ¡Compilación exitosa! El ejecutable se encuentra en: dist\Organizador.exe
    echo.
    pause
) else (
    echo.
    echo Error durante la compilación.
    pause
    exit /b 1
)
