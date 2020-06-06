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

Apellido= Label(text="Apellido",font=("Agency FB",14)).place(x=25,y=120)
Apellido=StringVar()
txtapellido=Entry(root,textvariable=Apellido)

Día= Label(text="Día",font=("Agency FB",14)).place(x=25,y=160)
Día=StringVar()
txdia=Entry(root,textvariable=Nombre,)

Mes = Label(text="Mes",font=("Agency FB",14)).place(x=25,y=220)
Mes=StringVar()
txtmes=Entry(root,textvariable=Nombre)