import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder

# from kivy.uix.behaviors.focus import FocusBehavior

from kivymd.uix.behaviors.focus_behavior import FocusBehavior



KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'MyApp'
            left_action_items: [["menu", lambda x: app.callback()]]
            right_action_items: [["dots-vertical", lambda x: app.callback_1()]]
        TelaLogin:

<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: .7,.7
    pos_hint: {'center_x':.5,'center_y':.5}

    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color

        MDLabel:
            text: 'Mudar Senha'
            theme_text_color: 'Custom'
            text_box: 1,1,1,1

        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()


    MDFloatLayout:
        MDTextField:

            size_hint_x: .9
            pos_hint: {'center_x': .5, 'center_y': .8}
            hint_text: 'Código Enviado por email.'

        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Digite uma nova senha'

        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar nova senha'


        MDRaisedButton:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            pos_hint: {'center_x': .5}
            text: 'Recadastrar'


<TelaLogin>:
    Image:
        source: 'trabalho.jpeg'
        allow_stretch: True
        size_hint:0.2, 0.2
        pos_hint: {'center_x':0.50,'center_y':0.78}
    FloatLayout:
        # MDIconButton:
        #     pos_hint:{'center_x':.5,'center_y':.8}
        #     icon:'language-python'
        #     users_font_size: '75sp'
    MDTextField:
        size_hint_x: .9
        hint_text: 'Email'
        pos_hint: {'center_x':.5,'center_y':.6}
    MDTextField:
        size_hint_x: .9
        hint_text: 'Senha'
        pos_hint: {'center_x':.5,'center_y':.5}



        
    ButtonFocus:
        size_hint_x: .9
        pos_hint: {'center_x':.5,'center_y':.4}
        text: 'Login'
        focus_color: app.theme_cls.accent_color
        unfocus_color:app.theme_cls.primary_color
    MDLabel:
        pos_hint: {'center_y': .3}
        halign: 'center'
        text: 'Esqueceu sua senha ?'
    MDTextButton:
        pos_hint: {'center_x': .5,'center_y': .2}
        text: 'Clique Aqui'
        on_release: root.abrir_card()
    

   

   


'''
class ButtonFocus(MDRaisedButton,FocusBehavior):
    ...

class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())

class myApp(MDApp):   
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Green'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    
myApp().run()

