from tkinter import *

root = Tk()

ancho = 400
alto = 270

root.geometry(str(ancho)+"x"+str(alto))
root.title("FINAL")

saludo = Label(text="Bienvenido",font=("Agency FB",14)).place(x=150,y=5)

lblname=Label(text="Nombre",font=("Agency FB",16)).place(x=80,y=30)
entrada=StringVar()
nombre =Entry(root,textvariable=entrada).place(x=135,y=40)

lblape=Label(text="Apellido",font=("Agency FB",16)).place(x=80,y=60)
entrada=StringVar()
apellido=Entry(root,textvariable=entrada).place(x=135,y=70)

lbldia=Label(text="Dia",font=("Agency FB",16)).place(x=80,y=90)
entrada=StringVar()
dia=Entry(root,textvariable=entrada).place(x=135,y=100)

lblmes=Label(text="Mes",font=("Agency FB",16)).place(x=80,y=120)
entrada=StringVar()
mes=Entry(root,textvariable=entrada).place(x=135,y=130)

lblaño=Label(text="Año",font=("Agency FB",16)).place(x=80,y=150)
entrada=StringVar()
año=Entry(root,textvariable=entrada).place(x=135,y=160)

btnFuncion1 = Button(root, text= "FUNCION 1",font=("Agency FB",10),width=10).place(x=90,y=180)
btnFuncion1 = Button(root, text= "FUNCION 2",font=("Agency FB",10),width=10).place(x=140,y=180)
btnFuncion1 = Button(root, text= "FUNCION 3",font=("Agency FB",10),width=10).place(x=190,y=180)
btnFuncion4 = Button(root, text= "FUNCION 4",font=("Agency FB",10),width=10).place(x=240,y=180)
btnFuncion5 = Button(root, text= "FUNCION 5",font=("Agency FB",10),width=10).place(x=290,y=180)
root.mainloop()


    