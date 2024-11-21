# Importa las librerías principales para la aplicación, el diseño y la navegación
from kivymd.app import MDApp  # Manejo de aplicaciones con KivyMD
from kivy.lang import Builder  # Carga de archivos de diseño KV
from kivymd.uix.screen import MDScreen  # Pantallas de la interfaz
from kivy.uix.screenmanager import ScreenManager  # Administrador de pantallas

# Importa herramientas adicionales para funcionalidad y propiedades
from kivy.properties import ObjectProperty  # Propiedades personalizadas
from plyer import filechooser  # Selector de archivos multiplataforma
from kivymd.uix.button import MDFlatButton  # Botones planos de KivyMD
from kivymd.uix.dialog import MDDialog  # Cuadros de diálogo de KivyMD


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
    pass  # Pantalla para reportar mascotas perdidas


class FoundPetScreen(BaseScreen):
    pass  # Pantalla para reportar mascotas encontradas


class HowItWorksScreen(BaseScreen):
    pass  # Pantalla para mostrar cómo funciona la aplicación


class MoreInfoScreen(BaseScreen):
    pass  # Pantalla para mostrar más información


# Clase para gestionar las pantallas en la aplicación
class Ui(ScreenManager):
    pass


# Clase principal de la aplicación
class MainApp(MDApp):
    def build(self):
        # Configuración del tema y estilo de la aplicación
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Light"

        # Carga el archivo KV desde la carpeta "templates"
        Builder.load_file("templates/design.kv")

        # Crea el administrador de pantallas y agrega las pantallas al mismo
        sm = Ui()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LostPetScreen(name="lost_pet"))
        sm.add_widget(FoundPetScreen(name="found_pet"))
        sm.add_widget(HowItWorksScreen(name="how_it_works"))
        sm.add_widget(MoreInfoScreen(name="more_info"))
        return sm  # Devuelve el ScreenManager para ser mostrado


# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    MainApp().run()
