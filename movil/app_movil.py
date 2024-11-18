from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from plyer import filechooser
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class BaseScreen(MDScreen):
    selected_file_label = ObjectProperty()

    def navigate(self, screen_name):
        self.parent.current = screen_name
        
    def show_selected_file(self, selection):
        if selection:
            self.selected_file_label.text = selection[0]
    
    def open_file_chooser(self):
        try:
            filechooser.open_file(
                on_selection=self.show_selected_file,
                filters=[("Imágenes", "*.png", "*.jpg", "*.jpeg")]
            )
        except Exception as e:
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


class HomeScreen(BaseScreen):
    pass


class LostPetScreen(BaseScreen):
    pass


class FoundPetScreen(BaseScreen):
    pass


class HowItWorksScreen(BaseScreen):
    pass


class MoreInfoScreen(BaseScreen):
    pass


class Ui(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Light"
        
        # Cargar el archivo KV
        Builder.load_file("design.kv")
        
        # Crear y configurar el ScreenManager
        sm = Ui()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LostPetScreen(name="lost_pet"))
        sm.add_widget(FoundPetScreen(name="found_pet"))
        sm.add_widget(HowItWorksScreen(name="how_it_works"))
        sm.add_widget(MoreInfoScreen(name="more_info"))
        return sm


if __name__ == "__main__":
    MainApp().run()