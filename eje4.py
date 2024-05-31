#Escribir una función que reciba una muestra
#de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados(lista):
    listaC=[]
    for i in lista:
        listaC.append(i**2)
    return listaC


listae=[12,3,4,5,6]
print(cuadrados(listae))

