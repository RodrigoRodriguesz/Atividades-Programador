# from PySimpleGUI import PySimpleGUI as sg
# #Layout
# sg.theme('Reddit')
# Layout = [
#     [sg.Text('Usuário'),sg.Input(key="usuario")],
#     [sg.Text('Senha'), sg.Input(key="senha", password_char='*')],
#     [sg.Checkbox("Salvar login? ")],
#     [sg.Button('Entrar')]
# ]

# nome = 'Rodrigo'

# janela = sg.Window('Tela de Login', Layout)
# while True:
#     eventos , valores = janela.read()
#     if eventos == sg.WINDOW_CLOSED:
#         break
#     if eventos== 'Entrar':
#         if valores['usuario'] == nome and valores ['senha'] == '123':
#             print(f"Bem-vindo"  , nome)
#         else:
#           print("Usuario inválido")
#         break  

