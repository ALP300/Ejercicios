from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")
    