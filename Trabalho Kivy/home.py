import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'

#BotãoDeNavegação:

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from View.Main_screen.MainScreen import MainScreenView

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm= MDScreenManager()
        self.load_all_kv_files(self.directory)

    def build(self):
        self.sm.add_widget(MainScreenView())
        self.theme_cls.material_style = 'M3'
        self.theme_cls.primary_palette= 'Orange'
        self.theme_cls.theme_style = "Light"
        return self.sm

MainApp().run()

