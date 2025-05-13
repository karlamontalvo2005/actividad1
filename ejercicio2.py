#Alumna: Karla Daniela Montalvo Macias
# **2. Conversión de temperatura (Celsius a Fahrenheit o Fahrenheit a Celsius)**
#Crea un programa que convierta una temperatura de **Celsius a Fahrenheit** o de **Fahrenheit a Celsius**, dependiendo de la elección del usuario.

#datos:
print(f"Ingresa un valor de temperatura:")
print(f"Seleccione una opcion:")
print(f"1.Celsius a Fahrenheit:")
print(f"2.Fahrenheit a Celsius:")

opcion = input("Ingrese el número de la opción: ")
if opcion == "1":
    celsius = float(input('Ingrese la temperatura en Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
elif opcion == "2":
    fahrenheit = float(input('Ingrese la temperatura en Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
else:
    print("Opción inválida.")