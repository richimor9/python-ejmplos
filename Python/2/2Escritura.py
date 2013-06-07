#Escritura en archivos
##Abrimos, pero tambien agregamos el parametro 'w'
agenda = open("Agenda.txt",'w')
#Selecionamos un metodo de Agenda
##agenda.truncate(), para borrar contenido(no es necesario)
agenda.truncate()
#recomendado cerrar el archivo
agenda.write("Este contenido lo escribimos desde IDLE")
agenda.close()
