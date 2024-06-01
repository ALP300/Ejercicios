from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self,marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo=tipo
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")