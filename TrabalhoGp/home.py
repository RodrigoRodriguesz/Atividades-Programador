import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'

#BotãoDeNavegação:

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from View.main_screen.MainScreen import MainScreenView

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm= MDScreenManager()

    def build(self):
        self.sm.add_widget(MainScreenView)

        return self.sm

MainApp().run()

