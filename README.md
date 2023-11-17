## Proyecto
Mente Sana: este proyecto propone desarrollar una plataforma web de salud mental en línea que ofrezca a los usuarios servicios de terapia profesional, meditación y comunidad, todo en un solo lugar.

## Descripción
En este repositorio se encuentrará el código fuente de los servicios backend de la plataforma. 
Consiste en una API desarrollada en el framework FastApi de Python, lo que nos garantiza un desarrollo rápido, de alto rendimiento y escalable.

## Software para ejecución
- Computadora con sistema operativo Windows, macOS o Linux
- Git
- Python versión 10+

## Backend project
```sh
git clone
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
En la terminal mostrará la url donde se iniciará el servidor, por lo general es: http://127.0.0.1:8000/

FastApi genera documentación de la API automáticamente, ingresar a http://127.0.0.1:8000/docs