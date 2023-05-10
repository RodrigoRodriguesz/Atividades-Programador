# import tkinter

# janela = tkinter.Tk()
# janela.geometry("500x300")
# texto = tkinter.Label(janela,text="Fazer Login")
# texto.pack(padx=10,pady=10)

# botao=tkinter.Button(janela,text="Login")
# botao.pack(padx=10,pady=10)

# janela.mainloop()

import customtkinter

janela = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
janela = customtkinter.CTk()
janela.geometry("650x500")
def clique():
    print("Conectado")

texto = customtkinter.CTkLabel(janela,text="Criar Cadastro: ",text_color='White')
texto.pack(padx=10,pady=10)

# botao=customtkinter.CTkButton(janela,text="Login")
# botao.pack(padx=10,pady=10)
Nome=customtkinter.CTkEntry(janela,placeholder_text="Seu Nome de Usuário")
Nome.pack(padx=10,pady=10)

cpf=customtkinter.CTkEntry(janela,placeholder_text="Seu CPF")
cpf.pack(padx=10,pady=10)

rg=customtkinter.CTkEntry(janela,placeholder_text="Seu RG")
rg.pack(padx=10,pady=10)

# Email=customtkinter.CTkEntry(janela,placeholder_text="Seu E-mail")
# Email.pack(padx=10,pady=10)

senha=customtkinter.CTkEntry(janela,placeholder_text="Sua Senha", show="*")
senha.pack(padx=10,pady=10)

checkbox=customtkinter.CTkCheckBox(janela,text="Manter Conectado")
checkbox.pack(padx=10,pady=10)

botao = customtkinter.CTkButton(janela,text="Login",command=clique)
botao.pack(padx=10,pady=10)


janela.mainloop()