print("////////// ACTIVIDAD 1 //////////")
print(" ")

# Función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 2 //////////")
print(" ")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 3 //////////")
print(" ")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresá el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = float(input("Ingresá una cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"

    return suma, resta, multiplicacion, division

# Programa principal
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

resultado = operaciones_basicas(a, b)

print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu IMC es: {imc:.2f}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 9 //////////")
print(" ")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Programa principal
celsius = float(input("Ingresá la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 10 //////////")
print(" ")

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio es: {promedio:.2f}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// FIN ACTIVIDADES FUNCIONES //////////")