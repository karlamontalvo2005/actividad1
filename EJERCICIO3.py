#Alumna: Karla Daniela Montalvo Macias
# **3. Perímetro y área de un rectángulo**
#Escribe un programa que calcule el **perímetro** y el **área** de un rectángulo, dados su largo y ancho. El programa debe validar que ambos valores sean positivos.
#datos:
largo=float(input('Cual es el largo del rectangulo:'))

ancho=float(input('Cual es el ancho del rectangulo:'))


#formulas
P = 2*(largo + ancho)
A = largo * ancho
#resultados
print(f"El área del rectangulo  es: {P}")
print(f"El perimetro del rectangulo  es: {A}")