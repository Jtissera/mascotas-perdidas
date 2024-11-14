#!/bin/bash

# --- Configuración inicial para la aplicación móvil en Kivy ---

# Instalación de dependencias para Kivy
echo "Instalando dependencias de Kivy..."
sudo apt install -y python3-pip python3-dev \
    build-essential git python3-setuptools python3-venv \
    libgles2-mesa libgles2-mesa-dev zlib1g-dev \
    libgstreamer1.0 libgstreamer-plugins-base1.0-dev \
    libmtdev-dev xclip libffi-dev

# Instalación de Kivy y otros paquetes necesarios
echo "Instalando Kivy y paquetes adicionales..."
pip install --upgrade pip
pip install kivy requests kivy-garden.mapview

# Instalación de Kivy Garden y componentes de MapView
echo "Instalando Kivy Garden y MapView..."
garden install mapview

