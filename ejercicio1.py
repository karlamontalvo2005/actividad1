#Alumna: Karla Daniela Montalvo Macias
#  **1. Área y perímetro de un círculo**
#Escribe un programa que calcule el **área** y el **perímetro** de un círculo, dado el valor de su radio. El programa debe validar que el radio sea un valor positivo.
#datos:
radio=float(input('Cual es el radio del circulo:'))
perimetro=float(input('Cual es el perimetro del circulo:'))
pi=3.1416

#formulas
area=pi*radio**2
per=2*pi*radio
#resultados
print(f"El área del círculo con radio {radio} es: {area}")
print(f"El perimetro del círculo con radio {radio} es: {per}")