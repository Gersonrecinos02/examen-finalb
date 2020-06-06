from tkinter import *

root = Tk()

ancho = 460
alto = 250

root.geometry(str(ancho)+"x"+str(alto))
root.title("FINAL")

saludo = Label(text="Bienvenido",font=("Agency FB",14)).place(x=150,y=5)

lblname=Label(text="Nombre",font=("Agency FB",14)).place(x=80,y=30)
entrada=StringVar()
txtnombre=Entry(root,textvariable=entrada).place(x=135,y=40)

lblape=Label(text="Apellido",font=("Agency FB",14)).place(x=80,y=60)
entrada=StringVar()
txtape=Entry(root,textvariable=entrada).place(x=135,y=70)

lbldia=Label(text="Dia",font=("Agency FB",14)).place(x=80,y=90)
entrada=StringVar()
txtdia=Entry(root,textvariable=entrada).place(x=135,y=100)

lblmes=Label(text="Mes",font=("Agency FB",14)).place(x=80,y=120)
entrada=StringVar()
txtmes=Entry(root,textvariable=entrada).place(x=135,y=130)

lblaño=Label(text="Año",font=("Agency FB",14)).place(x=80,y=150)
entrada=StringVar()
txtaño=Entry(root,textvariable=entrada).place(x=135,y=160)

btnFuncion1 = Button(root, text= "FUNCION 1",font=("Agency FB",10),width=10).place(x=80,y=180)
btnFuncion1 = Button(root, text= "FUNCION 2",font=("Agency FB",10),width=10).place(x=130,y=180)
btnFuncion1 = Button(root, text= "FUNCION 3",font=("Agency FB",10),width=10).place(x=180,y=180)
btnFuncion1 = Button(root, text= "FUNCION 4",font=("Agency FB",10),width=10).place(x=230,y=180)
btnFuncion1 = Button(root, text= "FUNCION 5",font=("Agency FB",10),width=10).place(x=280,y=180)

root.mainloop()