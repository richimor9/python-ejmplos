##Open tambien pide una entrada, pero en ves de pedir texto esta basada en un 
##archivo existente en el disco duro

##texto = open(info.txt)

texto = open("info.txt")

#Texto ahora es una instancia del objeto open, por lo tanto podemos
#usar alguno de sus metodos. eje: read(leer)
##Hacer texto.read() (usamos el metodo)

##Lo metemos dentro de una funcion, print
print(texto.read())


#Para leer de una carpeta superior
textoa = open("doc/sup.txt")
print(textoa.read())
#Para leer en una carpeta inferior
textob = open("../inf.txt")
print(textob.read())
#Para leer en una carpeta inferior y dentro de otra carpeta
textoa = open("../docu/den.txt")
print(textoa.read())
