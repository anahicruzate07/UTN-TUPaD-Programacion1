print("////////// ACTIVIDAD 1 //////////")
print(" ")

#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 2 //////////")
print(" ")

#pedir al usuario su nombre 
#imprimir por pantalla un saludo usando el nombre ingresado. 

nombre= input("Ingrese su nombre: ")
print(f"Hola, {nombre} !")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 3 //////////")
print(" ")

#pedir al usuario su nombre, apellido, edad y lugar de residencia 
#imprimir por pantalla una oración con los datos ingresados. 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("¿Cuántos años tiene?: ")
residencia = input("¿Dónde se reside actuallmente?: ")

print(" ")
print(f"Su nombre comprelo es {nombre} {apellido}, tiene {edad} años y vive en {residencia}.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

#pedir al usuario el radio de un círculo
#imprimir por pantalla su área y su perímetro.

import math

radio_txt = float(input("Por favor, ingrese el radio del círculo: "))

area_circulo = round(math.pi * (radio_txt)**2, 2)

perimetro_circulo = round(2 * math.pi * radio_txt, 2)

print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

#pedir al usuario una cantidad de segundos
#imprimir por pantalla a cuántas horas equivale.

seg_txt=input("Ingrese la cantidad de segundos: ")
seg=float(seg_txt)

hs=seg/3600

print(" ")
print(f"El equivalente de {seg_txt} segundos a horas es de {hs}.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

#pedir al usuario un número
#imprimir por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un número del que quiera saber su tabla de multiplicar: "))

n0 = num * 0
n1 = num * 1
n2 = num * 2
n3 = num * 3
n4 = num * 4
n5 = num * 5
n6 = num * 6
n7 = num * 7
n8 = num * 8
n9 = num * 9

print(f"""
  {num} x 0 = {n0}
  {num} x 1 = {n1}
  {num} x 2 = {n2}
  {num} x 3 = {n3}
  {num} x 4 = {n4}
  {num} x 5 = {n5}
  {num} x 6 = {n6}
  {num} x 7 = {n7}
  {num} x 8 = {n8}
  {num} x 9 = {n9}
      """)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

#pedir al usuario dos números enteros distintos del 0
#mostrar por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ingresar 2 números para sumar, restar, dividir y multiplicar")
print(" ")

n1=int(input("Ingrese su primer número entero: "))
n2=int(input("Ingrese su segundo número entero: "))

suma=n1+n2
divicion=n1/n2
multiplicacion=n1*n2
resta=n1-n2

print(" ")
print(f"A continuación, se mostrará los resultados de sus números: ")
print(f"Suma: {suma}.")
print(f"Resta: {resta}.")
print(f"Divición: {divicion}.")
print(f"Multiplicación: {multiplicacion}.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

#pedir al usuario su altura y su peso
#imprimir por pantalla su índice de masa corporal.
#tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))

imc=round(peso/(altura**2 , 2))
masa_corp=imc

print(" ")
print(f"Su masa corporal es de: {masa_corp}.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 9 //////////")
print(" ")

#pedir al usuario una temperatura en grados Celsius
#imprimir por pantalla su equivalente en grados Fahrenheit.
#Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temp_cel=float(input("Ingrese una temperatura en grados Celsius (sólo número): "))
temp_fhrt=9/5*temp_cel+32

print(" ")
print(f"Los grados Celsius equivalen a {temp_fhrt} grados fahrenheit.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 10 //////////")
print(" ")

#pedir al usuario 3 números
#imprimir por pantalla el promedio de dichos números.

print("Ingrese 3 números para calcular el promedio del total de los mismos.")
print(" ")

num_a=float(input("Ingrese su primer número:"))
num_b=float(input("Ingrese su segundo número:"))
num_c=float(input("Ingrese su tercer número:"))

promedio=(num_a+num_b+num_c)/3

print(" ")
print(f"El promedio de sus tres números es de: {promedio}.")

#fin----------------------------------------------------------------------------------------------------
print("////////// FIN ACTIVIDADES ESTRUCTURAS SECUENCIALES //////////")
