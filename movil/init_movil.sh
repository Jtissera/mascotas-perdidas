#!/bin/bash

# --- Configuración inicial para la aplicación móvil en Kivy ---

# Actualizar el sistema
sudo apt-get update

# Instalar las dependencias necesarias
sudo apt-get install -y python3 python3-pip

# Instalar las librerías de Python
pip3 install --upgrade pip setuptools wheel
pip3 install kivy
pip3 install kivymd
pip3 install plyer
pip install kivy-garden.mapview
chmod +x /home/franco/Escritorio/mascotas-perdidas/movil/.kivy/bin/garden
garden install mapview

echo "Todas las librerías necesarias han sido instaladas."


