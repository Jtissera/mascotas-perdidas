# Importa las librerías principales para la aplicación, el diseño y la navegación
from kivymd.app import MDApp  # Manejo de aplicaciones con KivyMD
from kivy.lang import Builder  # Carga de archivos de diseño KV
from kivymd.uix.screen import MDScreen  # Pantallas de la interfaz
from kivy.uix.screenmanager import ScreenManager  # Administrador de pantallas

import requests
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapMarkerPopup #sirve para aniadir marcadores al mapa
from kivy.uix.label import Label


# Importa herramientas adicionales para funcionalidad y propiedades
from kivy.properties import ObjectProperty  # Propiedades personalizadas
from plyer import filechooser  # Selector de archivos multiplataforma
from kivymd.uix.button import MDFlatButton  # Botones planos de KivyMD
from kivymd.uix.dialog import MDDialog  # Cuadros de diálogo de KivyMD

API_URL = "http://localhost:8080/"
# Clase base para las pantallas de la aplicación
class BaseScreen(MDScreen):
    # Define una propiedad para mostrar el archivo seleccionado
    selected_file_label = ObjectProperty()

    # Método para cambiar entre pantallas
    def navigate(self, screen_name):
        self.parent.current = screen_name

    # Método para actualizar el texto con el archivo seleccionado
    def show_selected_file(self, selection):
        if selection:  # Verifica si hay una selección válida
            self.selected_file_label.text = selection[0]

    # Método para abrir el selector de archivos y filtrar imágenes
    def open_file_chooser(self):
        try:
            # Abre el selector de archivos con un filtro para imágenes
            filechooser.open_file(
                on_selection=self.show_selected_file,
                filters=[("Imágenes", "*.png", "*.jpg", "*.jpeg")]
            )
        except Exception as e:
            # Muestra un cuadro de diálogo en caso de error
            dialog = MDDialog(
                title="Error",
                text="No se pudo abrir el selector de archivos.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: dialog.dismiss()
                    )
                ]
            )
            dialog.open()


# Clases para las diferentes pantallas de la aplicación
class HomeScreen(BaseScreen):
    pass  # Pantalla de inicio


class LostPetScreen(BaseScreen):
    def on_enter(self):
        """Se llama automáticamente cuando se entra en esta pantalla."""
        self.load_pets_from_backend()

    def load_pets_from_backend(self):
        """Carga las mascotas desde el backend."""
        try:
            # Reemplaza con la URL de tu API de backend
            response = requests.get(API_URL + "/mascotas")
            mascotas = response.json()  # Asumiendo que la API devuelve un JSON con las mascotas

            mascotas_grid = self.ids.mascotas_grid
            mascotas_grid.clear_widgets()

            for mascota in mascotas:
                ficha_mascota = self.crear_ficha_mascota(mascota)
                mascotas_grid.add_widget(ficha_mascota)
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con el backend: {e}")

    def crear_ficha_mascota(self, mascota):
        """Crea un widget para representar una mascota."""
        ficha = MDCard(
            orientation="vertical",
            size_hint=(None, None),
            size=("120dp", "150dp"),
            ripple_behavior=True,
            on_release=lambda *args: self.show_pet_details(mascota),
        )
        ficha.add_widget(
            Image(
                source= "../frontend/" + mascota["imagen"],  # Ruta a la imagen de la mascota
                size_hint=(1, 0.8),
                allow_stretch=True,
                keep_ratio=True,
            )
        )
        ficha.add_widget(
            MDLabel(
                text=mascota["nombre"],  # Nombre de la mascota
                halign="center",
                size_hint_y=0.2,
            )
        )
        return ficha

    def show_pet_details(self, mascota):
        """Muestra detalles de la mascota seleccionada."""
        # Accede al ScreenManager y cambia a la pantalla de detalles
        pet_details_screen = self.manager.get_screen("pet_details")
        pet_details_screen.set_pet_data(mascota)
        self.manager.current = "pet_details"  # Cambia a la pantalla de detalles


class FoundPetScreen(BaseScreen):
    pass  # Pantalla para reportar mascotas encontradas


class HowItWorksScreen(BaseScreen):
    pass  # Pantalla para mostrar cómo funciona la aplicación


class MoreInfoScreen(BaseScreen):
    pass  # Pantalla para mostrar más información


# Clase para gestionar las pantallas en la aplicación
class Ui(ScreenManager):
    pass

class PetDetailsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pet = None  # Variable para almacenar los datos de la mascota

    def on_pre_enter(self, *args):
        """Se llama antes de que la pantalla sea cargada."""
        # Aquí puedes actualizar los datos según la mascota seleccionada
        if self.pet:
            self.ids.animal_nombre.text = self.pet["nombre"]
            self.ids.animal_descripcion.text = self.pet["descripcion"]
            self.ids.animal_imagen.source = "../frontend/" + self.pet["imagen"]
            self.ids.animal_edad.text = self.pet["edad"]
            self.ids.animal_animal.text = self.pet["animal"]
            self.ids.animal_raza.source = self.pet["raza"]
            self.ids.animal_fecha.text = self.pet["fecha"]
            self.ids.animal_color.text = self.pet["color"]


            map_view = self.ids.pet_map
            map_view.lat = self.pet["latitud"]
            map_view.lon = self.pet["longitud"]
            
            marker = MapMarkerPopup(lat=self.pet["latitud"], lon=self.pet["longitud"]) #crea el marcador de la mascota
            popup_label = Label(text=self.pet["nombre"], size_hint=(None, None), size=(150, 50), color=(1, 0, 0, 1)) #le da estilos
            marker.add_widget(popup_label)

            map_view.add_widget(marker)
            
    def set_pet_data(self, pet):
        """Establece los datos de la mascota que se mostrarán en la pantalla."""
        self.pet = pet


# Clase principal de la aplicación
class MainApp(MDApp):
    def build(self):
        # Configuración del tema y estilo de la aplicación
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Light"

        # Carga el archivo KV desde la carpeta "templates"
        Builder.load_file("frontend/templates/design.kv")

        # Crea el administrador de pantallas y agrega las pantallas al mismo
        sm = Ui()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LostPetScreen(name="lost_pet"))
        sm.add_widget(FoundPetScreen(name="found_pet"))
        sm.add_widget(HowItWorksScreen(name="how_it_works"))
        sm.add_widget(MoreInfoScreen(name="more_info"))
        sm.add_widget(PetDetailsScreen(name="pet_details"))
        return sm  # Devuelve el ScreenManager para ser mostrado


# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    MainApp().run()