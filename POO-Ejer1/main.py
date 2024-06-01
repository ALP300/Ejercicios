from coche import Coche
from motocicleta import Motocicleta
from camion import Camion
def main():
    coche= Coche("Audi","R8 Coupé","2022","2")
    motocicleta= Motocicleta("Yamaha","Yamaha","2019","Deportivo")
    camion= Camion("Volvo","Volvo","2020","4000")
    
    print("Información del coche: ")
    coche.mostrar_info()
    
    print("\nInformación de la motocicleta: ")
    motocicleta.mostrar_info()
    
    print("\nInformación del camión: ")
    camion.mostrar_info()
    


main()