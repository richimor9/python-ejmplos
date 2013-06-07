agenda = open("Agendal.csv")

#Estructura for:
#1.-Declaramos una variable en este caso "i"
#2.-Especificamos en que rango se movera, en este caso (0,4)
#Son cuatro registros


for i in range(0,25):
    print(agenda.readline())
#La sangria tambien es roconociada por python, la ultima linea
#esta fuera de la sangria, por lo que solo aparecera 1 ves
print("\nSe concluyo la lectura de archivos")
