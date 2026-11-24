# Imagen Base: Python3.12 - version ligera (Debian)
FROM python:3.12-slim

# No generar .pyc y mostrar logs al instante
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

# Carpeta de trabajo
WORKDIR /code

# Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo fuente
COPY app ./app

# Puerto en el que escucha la PAI dentro del contenedor
EXPOSE 8000

# fastapi run escuche en 0.0.0.0 (y no en 127.0.0.1)
CMD [ "fastapi", "run", "app/main.py", "--port", "8000" ]