#!/bin/bash

# --- Configuración inicial para la aplicación móvil en Kivy ---

# 1. Actualización de paquetes
echo "Actualizando paquetes del sistema..."
sudo apt update && sudo apt upgrade -y

# 2. Instalación de dependencias para Kivy
echo "Instalando dependencias de Kivy..."
sudo apt install -y python3-pip python3-dev \
    build-essential git python3-setuptools python3-venv \
    libgles2-mesa libgles2-mesa-dev zlib1g-dev \
    libgstreamer1.0 libgstreamer-plugins-base1.0-dev \
    libmtdev-dev xclip libffi-dev

# 3. Creación de un entorno virtual
echo "Creando un entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# 4. Instalación de Kivy y otros paquetes necesarios
echo "Instalando Kivy y paquetes adicionales..."
pip install --upgrade pip
pip install kivy requests kivy-garden.mapview

# 5. Instalación de Kivy Garden y componentes de MapView
echo "Instalando Kivy Garden y MapView..."
garden install mapview

# 6. Confirmación de la instalación
echo "Configuración completada. Activa el entorno virtual usando: source venv/bin/activate"
