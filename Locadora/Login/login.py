import customtkinter
import PIL
from tkinter import * 

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")

jan = customtkinter.CTk()
jan.geometry("700x400")
jan.title("login")


# jan.iconbitmap("icon.ico")
# jan.resizable(False,False)

#Foto

img = customtkinter.CTkImage(PIL.Image.open(fp="C:/Users/Cateq-2/Documents/Locadora/Login/lokcorn.png"),size=(150,221))
label_img= customtkinter.CTkLabel(master=jan,image=img, compound="center", text="" )
label_img.place(x=5,y=65)
# frames
# frame=customtkinter.CTkFrame(master=jan,width=350,height=396)
# frame.place(side=RIGHT)

# label = customtkinter.CTkLabel(master=frame,text="Sistema de Login", text_font=("Roboto",20))
# label.place(x=25,y=5)

# entry1= customtkinter.CTkEntry(master=frame,placeholder_text="Nome de Usuario: ", width=300,text_font=('Roboto', 14)).place(x=25,y=105)
# label1=customtkinter.CTkLabel(master=frame,text="O campo nome de usuario é obrigatório.",text_color="green",text_font=("Reboto",8)).place(x=25,y=105)

jan.mainloop()