#Externando funciones----->

def bienvenidos():
    print("Bienvenido a Agenda telefonica")
    print("\nSelecciona una opcion:\n")
    print("1- Añadir un registro a la agenda")
    print("2- Listar el contenido de la agenda")
    print("3- Buscar por nombre")


def escribir():
    print("\nHas elejido añadir un registro a la agenda")   
    nombre   = input("Nombre del contacto: ")
    tele     = input("Telefono del contacto: ")

    agenda   = open("Agendal.csv")
    for n in range(1,40):
        linea = agenda.readline()
        lineapartida = linea.split(",")
        #print(lineapartida[0])
        

        if lineapartida[0] != "":
            memoria = lineapartida[0]

            
    #print("El numero maximo es: ",memoria)
    agenda.close()
    memonum = int(memoria)
    posicion = 0
    posicion = memonum + 1
    postr = str(posicion)
    print("Se ha guardado el contacto",nombre,"Con el tel: ",tele)
   
    agenda   = open("Agendal.csv",'a')
    agenda.write("\n")
    agenda.write(postr)
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(tele)
    #agenda.write(",")
    #agenda.write("\n")
    agenda.close()


def listar(fin):
    print("\nHas elejido listar el contenido de la agenda")
    agenda = open("Agendal.csv")
    numero = 0
    for i in range(1,fin):
        #print(agenda.readline())
        #Creamos una variable que guarda las lineas, con replace
        #cambiamos las "," por "\t\t"
        lectura = agenda.readline()
        print(lectura.replace(",","\t\t"))
        numero = numero + 1
    print("\nSe concluyo la lectura de archivos")
    agenda.close()

def mierror():
    print("La opcion que has seleccionado no es valida...")

def buscador(nombrebuscado):
    print("coincidencias")
    agenda = open("Agendal.csv")
    for i in range(1,30):
        lectura = agenda.readline()
        partido = lectura.split(',')
        if nombrebuscado == partido[1]:
            print(partido[2])
    agenda.close()
                
