agenda = open("Agendal.csv",'w')

#recordando(ejer)...
nombre = input("Nombre del contacto: ")
tele   = input("Telefono del contacto: ")

print("Se ha guardado el contacto",nombre,"Con el tel: ",tele)
##agenda.write(nombre,",",tel,"\n")
agenda.write(nombre)
agenda.write(",")
agenda.write(tele)
agenda.write(",")
agenda.write("\n")
agenda.close()


#Modo de añadido
#Cambiamos 'w' por 'a' de agregar y no borrar contenido
#csv por Excel
