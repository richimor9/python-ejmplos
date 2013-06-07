agenda = open("Agendal.csv")

numero = 0

while numero < 25:
    print(agenda.readline())
    numero = numero + 1
    
print("\nSe concluyo la lectura de archivos")

#A diferencia del for este no incluye la condiciones de inicio y fin,
#While seguira ejecutandoce hasta que de manera interna le indiquemos
#que pare
