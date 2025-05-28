FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script
COPY festak.py .

# Hacer el script ejecutable
RUN chmod +x festak.py

# Entrypoint para asegurar que el script se ejecute correctamente
CMD ["python3", "festak.py"]

# Mantener el contenedor abierto
CMD ["tail", "-f", "/dev/null"]
