#Escribir un programa que permita gestionar la base de datos de clientes
# de una empresa. Los clientes se guardarán en un diccionario en el 
# que la clave de cada cliente será su NIF, y el valor será otro 
# diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
# (4) Listar todos los clientes, (5) Listar clientes preferentes, 
# (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

clientes={}
opcion=''
while opcion!='6':
    if opcion=='1':
        nif=input("Introduce NIF: ")
        nombre=input("Introduce nombre: ")
        direccion=input("Introduce direccion: ")
        telefono=input("Introduce telefono: ")
        correo=input("Introduce correo: ")
        vip= input("¿Es un cliente preferente (S/N)?: ")
        cliente={'nombre':nombre,'direccion':direccion,'telefono':telefono,'correo':correo,'preferente':vip=='S'}
        clientes[nif]=cliente
    
    if opcion=='2':
        nif=input("Introduce NIF: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("No existe el cliente con el nif: ",nif)
    
    if opcion=='3':
        nif=input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF: ',nif)
            for clave, valor in clientes[nif].items():
                print(clave.title()+':',valor)
        else:
            print("No existe el cliente con el nif: ",nif)
        
        
    if opcion=='4':
        print("Listar clientes")
        for clave, valor in clientes.items():
            print(clave,valor['nombre'])
            
            
    if opcion=='5':
        print("Listar clientes preferentes: ")
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave,valor['nombre'])
    
    opcion=input("Menú de opciones\n(1) Añadir clientes\n(2) Eliminar Clientes\n(3)Mostrar Cliente\n(4)Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción: ")
