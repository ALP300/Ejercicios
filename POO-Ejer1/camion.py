from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de carga: {self.capacidad_carga} kg")