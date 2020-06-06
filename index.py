from tkinter import *

root = Tk()
root.title("Examen final")
root.geometry("600x500")

miFrame = Frame()

miFrame.pack()


Saludo = Label(text="Bienvenidos",font=("Agency6 FB",25)).place(x=250,y=30)



def Resultado():
    Label(root,text=""+Nombre()+' es impar y '+Apellido()+'es impar',font=("Agency Fb",14)).place(x=25,y=120)
    

Nombre= Label(text="Nombre",font=("Agency FB",14)).place(x=25,y=80)
Nombre=StringVar()
txtnombre=Entry(root,textvariable=Nombre,width=34)





