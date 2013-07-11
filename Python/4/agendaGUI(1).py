#Python 2 se importa como Tkinter y Python 3 tkinter
#Con el . llamamos a los metodos (de Frame)

from tkinter import *
import ModdeAg

def escribe():
    lista.insert(END,"Hola")

def listar():
    agenda = open("Agendal.csv")
    numero = 0
    for i in range(1,30):
        lectura = agenda.readline()
            #print(lectura.replace(",","\t\t"))
        lista.insert(END,lectura.replace(",","   "))
        numero = numero + 1
    agenda.close()
    
f = Frame(height=300,width=300)
f.pack(padx=15, pady=15)

logoimg = PhotoImage(file="logo.gif")
etiquetalogo = Label(f, image = logoimg)
etiquetalogo.pack(side=TOP,padx=10,pady=10)

titulo = Label(f, text="Agenda Telefonica",fg="blue",font=("Arial",24))
titulo.pack(side=TOP,padx=10,pady=10)

autor = Label(f, text="Juan de Dios")
autor.pack(side=TOP,padx=10,pady=10)

campo = Entry(f,textvariable = 5)
campo.pack(side=TOP,padx=10,pady=10)

#boton1 = Button(f,text="Listar elementos de la agenda",command=lambda:ModdeAg.listar(int(Entry.get(campo))))
boton1 = Button(f,text="Listar elementos de la agenda",command=listar)
boton1.pack(side=BOTTOM,padx=10,pady=10)

lista = Listbox(f)
lista.pack(side=TOP,padx=10,pady=10)
