# --- Importaciones ---
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle 
from kivy.garden.mapview import MapView, MapMarker
from kivy.clock import Clock
import requests

# --- Clases para la UI de Mascotas ---



# --- Ejecución de la Aplicación ---
if __name__ == '__main__':
    AplicacionPrincipal().run()
