# Stockholm

Stockholm es un programa de cifrado de archivos para Linux y MacOS que actúa sobre una carpeta llamada `infection` en el directorio HOME del usuario.

## Requisitos

- Python 3.6 o superior
- cryptography (`pip install cryptography`)

## Uso

1. Coloca los archivos que deseas cifrar en la carpeta `infection` dentro de tu directorio HOME.
2. Ejecuta el programa: `python stockholm.py`
3. El programa mostrará una clave de cifrado. Guárdala en un lugar seguro.
4. Para descifrar los archivos, ejecuta el programa con la opción `-r` o `--reverse` seguida de la clave de cifrado: `python stockholm.py -r TU_CLAVE`

## Opciones

- `-h`, `--help`: Muestra la ayuda del programa.
- `-v`, `--version`: Muestra la versión del programa.
- `-s`, `--silent`: No muestra ningún output durante el proceso de cifrado/descifrado.
- `-r KEY`, `--reverse KEY`: Revierte la infección utilizando la clave proporcionada.