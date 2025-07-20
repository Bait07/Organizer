## Organizador de Archivos

Aplicación simple para organizar automáticamente archivos en carpetas según su tipo y fecha de modificación.

(SI QUIERE USAR EL EL PROGRAMA, DESCARGUE EL .EXE DE LA CARPETA dist)

## Características

- Organiza archivos por tipo (documentos, imágenes, música, videos, etc.)
- Suborganización por fecha de modificación (Año-Mes)
- Interfaz gráfica simple y fácil de usar
- Muestra progreso en tiempo real
- Manejo de archivos duplicados

## Requisitos

- Python 3.13 o superior
- Windows (puede funcionar en otros sistemas operativos con pequeñas modificaciones)

## Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar desde el código fuente

1. Navega a la carpeta `src` del proyecto:
   ```
   cd src
   ```
2. Ejecuta el programa:
   ```
   python main.py
   ```
3. Haz clic en "Examinar" y selecciona la carpeta que deseas organizar
4. Haz clic en "Comenzar" para iniciar la organización
5. Espera a que el proceso termine

### Crear un ejecutable (.exe)

Para crear un archivo ejecutable que puedas compartir o usar sin necesidad de tener Python instalado:

1. Asegúrate de tener instalado PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Navega a la carpeta `src` del proyecto:
   ```
   cd src
   ```

3. Ejecuta el script de compilación:
   ```
   .\build.bat
   ```
   Esto creará un archivo ejecutable en la carpeta `dist`.

4. Si el script falla, asegúrate de que:
   - Tienes Python instalado en `C:\Python313`
   - Los directorios `C:\Python313\tcl\tcl8.6` y `C:\Python313\tcl\tk8.6` existen

5. Una vez compilado, encontrarás el ejecutable en:
   ```
   dist\Organizador.exe
   ```

   Puedes copiar este archivo a cualquier ubicación y ejecutarlo directamente.

## Estructura de Carpetas

Los archivos se organizarán de la siguiente manera:
```
CarpetaSeleccionada/
├── Documentos/
│   ├── PDF/
│   │   ├── 2023-01/
│   │   ├── 2023-02/
│   │   └── ...
│   ├── Word/
│   └── ...
├── Imágenes/
│   ├── 2023-01/
│   └── ...
├── Música/
├── Videos/
├── Comprimidos/
├── Programas/
└── Otros/
```

## Crear Ejecutable (opcional)

Para crear un archivo .exe que puedas ejecutar sin necesidad de Python:

1. Asegúrate de tener PyInstaller instalado (viene en requirements.txt)
2. Ejecuta:
   ```
   pyinstaller --onefile --windowed --icon=icon.ico main.py
   ```
3. El ejecutable estará en la carpeta `dist/`

## Notas

- El programa no modifica archivos, solo los mueve entre carpetas
- Se recomienda hacer una copia de seguridad antes de usar en carpetas importantes
- Los archivos con el mismo nombre se renombrarán automáticamente (ej: archivo_1.pdf, archivo_2.pdf)

## Licencia

Este proyecto está bajo la Licencia MIT.

## Créditos

Programado por Juan Diego Enríquez - 2025
