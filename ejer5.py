def cuadrados(lista):
    listaCuadrados=[]
    for i in lista:
        listaCuadrados.append(i**2)
    return listaCuadrados


print(cuadrados([1,2,3,4,5]))