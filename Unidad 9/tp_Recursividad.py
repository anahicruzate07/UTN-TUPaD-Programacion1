print("////////// ACTIVIDAD 1 //////////")
print(" ")

# Función recursiva que calcule el factorial de un número.
# Utilizar esa función para calcular y mostrar en pantalla el factorial 
#de todos los números enteros entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Programa 
numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero + 1):
    print(f"El factorial de {i} es: {factorial(i)}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 2 //////////")
print(" ")

# Función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

# Programa 
numero = int(input("Ingrese la posición hasta donde desea mostrar Fibonacci: "))

print("Serie de Fibonacci:")

for i in range(numero + 1):
    print(fibonacci(i), end=" ")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 3 //////////")
print(" ")

# Función recursiva que calcule la potencia de un número base elevado a un exponente, 
#utilizando la fórmula " 𝑛𝑚= 𝑛∗𝑛(𝑚−1) ". Probar esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa 
numero = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(numero, exponente)

print(f"El resultado de {numero} elevado a {exponente} es: {resultado}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

# Función recursiva en Python que reciba un número entero positivo en base decimal 
#y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(numero):
    if numero < 2:
        return str(numero)
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

# Programa 
numero = int(input("Ingrese un número entero positivo: "))

resultado = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {resultado}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

# Implementar una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Programa 
palabra = input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

# Escribir una función recursiva en Python llamada " suma_digitos(n) " 
#que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
#   suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#   suma_digitos(9) → 9
#   suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Programa
numero = int(input("Ingrese un número entero positivo: "))

resultado = suma_digitos(numero)

print(f"La suma de los dígitos de {numero} es: {resultado}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

# Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel 
# uno menos " (n - 1) ", y así sucesivamente hasta llegar al último nivel con un solo bloque.

# Escribir una función recursiva contar_bloques(n) que reciba el número de bloques 
#en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
#   contar_bloques(1) → 1 (1)
#   contar_bloques(2) → 3 (2 + 1)
#   contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Programa
numero = int(input("Ingrese la cantidad de bloques del nivel inferior: "))

resultado = contar_bloques(numero)

print(f"La pirámide necesita {resultado} bloques.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

# Escribir una función recursiva llamada " contar_digito(numero, digito) "
#que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
#y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
#   contar_digito(12233421, 2) → 3
#   contar_digito(5555, 5) → 4
#   contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Programa
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea buscar (0 al 9): "))

resultado = contar_digito(numero, digito)

print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// FIN ACTIVIDADES RECURSIVIDAD //////////")
