#Agenda telefonica
#v0.1 por Juan de Dios Torres Menchaca

import ModdeAg

def principal():    
    ModdeAg.bienvenidos()
    opcion = input("\n>")
    print("\nHaz seleccionado la opcion: ",opcion)


    if opcion == "1":
        ModdeAg.escribir()
        principal()
    elif opcion == "2":cxseksjksj
        print("\nCuantos numeros quieres ver:")
        registros = input("\n>")
        registrosnum = int(registros)
        ModdeAg.listar((registrosnum+1))
        principal()
    elif opcion == "3":
        print("\nDime el nombre que estas buscando:")
        nombrebuscado = input("\n>")
        ModdeAg.buscador(nombrebuscado)
        principal()
    else:
        ModdeAg.mierror()
        principal()
principal()

