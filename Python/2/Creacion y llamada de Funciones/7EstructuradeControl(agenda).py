#Agenda telefonica
#v0.1 por Juan de Dios Torres Menchaca

def bienvenidos():
    print("Bienvenido a Agenda telefonica")
    print("\nSelecciona una opcion:\n")
    print("1- Añadir un registro a la agenda")
    print("2- Listar el contenido de la agenda")

bienvenidos()
bienvenidos()
opcion = input("\n>")

print("\nHaz seleccionado la opcion: ",opcion)

#################################################################
if   opcion == "1":
    print("\nHas elejido añadir un registro a la agenda")
    agenda = open("Agendal.csv",'a')

    nombre   = input("Nombre del contacto: ")
    tele     = input("Telefono del contacto: ")
    posicion = input("Posicion del contacto: ")

    print("Se ha guardado el contacto",nombre,"Con el tel: ",tele)

    agenda.write(posicion)
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(tele)
    agenda.write(",")
    agenda.write("\n")
    agenda.close()
#################################################################
elif opcion == "2":
    print("\nHas elejido listar el contenido de la agenda")
    agenda = open("Agendal.csv")
    numero = 0
    
    while numero < 30:
        #print(agenda.readline())
        #Creamos una variable que guarda las lineas, con replace
        #cambiamos las "," por "\t\t"
        lectura = agenda.readline()
        print(lectura.replace(",","\t\t"))
        numero = numero + 1
    print("\nSe concluyo la lectura de archivos")
    agenda.close()
#################################################################
else:
    print("La opcion que has seleccionado no es valida...")
