 #Escribir una función que reciba 
 # un número entero positivo y devuelva su factorial.
 
def factorial(n):
     num=1
     for i in range(n):     
         num*=i+1
     return num
  

numero= int(input("Introduce el número: "))   
print(factorial(numero))
     
    