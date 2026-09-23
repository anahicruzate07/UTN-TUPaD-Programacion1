print("////////// ACTIVIDAD 1 //////////")
print(" ")

#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0, 101):
    print(numero)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 2 //////////")
print(" ")

#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = abs(int(input("Introduce un número entero: ")))

contador_digitos = 0

if numero == 0:
    contador_digitos = 1
else:
    while numero > 0:
        numero //= 10 
        contador_digitos += 1

print(f"El número tiene {contador_digitos} dígitos.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 3 //////////")
print(" ")

#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

inicio = int(input("Introduce el primer número (límite inferior): "))
fin = int(input("Introduce el segundo número (límite superior): "))

if inicio > fin:
    inicio, fin = fin, inicio

suma_total = 0

for i in range(inicio + 1, fin):
    suma_total += i

print(f"La suma de los números entre {inicio} y {fin} (excluyéndolos) es: {suma_total}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma_acumulada = 0

print("Introduce números para sumar. Escribe '0' para finalizar.")

while True:
    numero = int(input("Ingresa un número entero: "))
    
    if numero == 0:
        break 
    
    suma_acumulada += numero
    print(f"Suma parcial: {suma_acumulada}")

print("-" * 20)
print(f"PROCESO TERMINADO. El total acumulado es: {suma_acumulada}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)

intentos = 0
print("Pensé un número entre 0 y 9! Adivínalo!")

while True:
    intento_usuario = int(input("Introduce tu número: "))
    intentos += 1
    
    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! Acertaste el número: {numero_secreto}.")
        break 
    elif intento_usuario < numero_secreto:
        print("Uh... mi número es mayor.")
    else:
        print("No, mi número es menor.")

print(f"Lograste adivinarlo en {intentos} intentos.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

limite = int(input("Introduce un número entero positivo: "))

suma_total = 0

for i in range(0, limite + 1):
    suma_total += i 

print(f"La suma de todos los números desde 0 hasta {limite} es: {suma_total}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantid_total = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Por favor, ingresa {cantid_total} números enteros:")

for i in range(cantid_total):
    num = int(input(f"Número {i + 1}: "))
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("-" * 30)
print(f"Resultados para {cantid_total} números:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 9 //////////")
print(" ")

#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad_procs = 100

# Necesitamos una variable para ir acumulando la suma
suma_acumulada = 0

print(f"Vas a ingresar {cantidad_procs} números para calcular su media.")

# Bucle para solicitar los números
for i in range(cantidad_procs):
    # Pedimos el número (i+1 es solo para que el usuario vea "Número 1", "Número 2"...)
    numero = int(input(f"Ingresa el número {i + 1}: "))
    
    # Vamos sumando cada número al total
    suma_acumulada += numero

# Calculamos la media (Suma total / Cantidad)
media = suma_acumulada / cantidad_procs

print("-" * 30)
print(f"La suma total es: {suma_acumulada}")
print(f"La media aritmética es: {media}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 10 //////////")
print(" ")

#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Introduce un número entero para invertir: "))

es_negativo = numero < 0
n = abs(numero)

numero_invertido = 0

while n > 0:
    ultimo_digito = n % 10
    
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    
    n //= 10

if es_negativo:
    numero_invertido *= -1

print(f"El número invertido es: {numero_invertido}")

#fin----------------------------------------------------------------------------------------------------
print("////////// FIN ACTIVIDADES ESTRUCTURAS SECUENCIALES //////////")
