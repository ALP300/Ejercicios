#Ejercicio: Sistema de Vehículos
#Imagina que estás diseñando un sistema para gestionar diferentes tipos de vehículos. Debes crear una jerarquía de clases para representar distintos tipos de vehículos y sus características. Aquí están los detalles del ejercicio:
#Clase Base: Vehículo
#Atributos:
#marca (cadena)
#modelo (cadena)
#año (entero)
#Métodos:
#mostrar_info(): Muestra la información del vehículo.
##Clase Derivada: Coche
#Hereda de: Vehículo
#Atributos adicionales:
#puertas (entero)
#Métodos:
#mostrar_info(): Muestra la información del coche incluyendo el número de puertas.
#Clase Derivada: Motocicleta
#Hereda de: Vehículo
#Atributos adicionales:
#tipo (cadena, por ejemplo, "deportiva", "crucero")
#Métodos:
#mostrar_info(): Muestra la información de la motocicleta incluyendo el tipo.
#Clase Derivada: Camión
#Hereda de: Vehículo
#Atributos adicionales:
#capacidad_carga (entero, en kilogramos)
#Métodos:
#mostrar_info(): Muestra la información del camión incluyendo la capacidad de carga.

class Vehiculo:
    def __init__(self,marca, modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}")
            
        
        