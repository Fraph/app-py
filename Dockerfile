# 1. Usamos una imagen base ligera de Python
FROM python:3.11-slim

# 2. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos los archivos de tu ordenador al contenedor
COPY . .

# 4. Comando para ejecutar la aplicación
CMD ["python", "app.py"]
