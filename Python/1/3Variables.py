#Variable

edad = 24
edad2 = "24"
nombre = "Juand"
ap = "Torres"

print(nombre,"con:",edad, "años")

#Concatenacion

##print("Mi nombre es: " + nombre + "y tengo: " + edad + "años")

print("Mi nombre es: " + nombre + " y tengo: " + edad2 + " años")


##La coma marca un espacio.
print("Mi nombre es: ",nombre, "y tengo: ",edad,"años")
print("Su nombre es: ",nombre, "y tiene: ",edad,"años","y el doble de su edad es:",(edad*2),"años")


#Formateo de variables
#Llamar a una cadena como un String
print("Mi nombre es: %s"%nombre)
print("Mi nombre completo es: %s %s"%(nombre,ap))

#No recomendado, se esta cambiando una variable del tipo int a string
#print("Mi nombre es: %s y tengo:%s" %(nombre,edad))
print("Mi nombre es: %s y tengo:%d y la mitad de mi edad es: %d" %(nombre,edad,edad/2))

