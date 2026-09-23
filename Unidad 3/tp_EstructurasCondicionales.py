print("////////// ACTIVIDAD 1 //////////")
print(" ")

#solicitar la edad del usuario. 
#usuario mayor de 18 años:
#mensaje que diga “Es mayor de edad”.

edad=int(input("Por favor, ingrese su edad (sólo número): "))

if edad < 18 :
    print("Usted no es mayor.") 
else :
    print("Es mayor de edad.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 2 //////////")
print(" ")

#solicitar su nota al usuario.
#mayor o igual a 6, mensaje “Aprobado”.
#contrario, mensaje “Desaprobado”.

nota_usser=int(input("Ingrese su nota de examen: "))

if nota_usser>=6 :
    print("Aprobado.")
else :
    print("Desaprobado.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 3 //////////")
print(" ")

#NOTA: investigar el uso del operador de módulo (%)
#para evaluar si un número es par o impar.

#ingresar solo números pares.
#si ingresa número par: imprimir mensaje "Ha ingresado un número par".
#si ingresa número impar: imprimir mensaje "Por favor, ingrese un número par".

numero=1

while numero % 2 !=0:
    numero=int(input("Por favor, ingrese un número par: "))

    if numero % 2 == 0:
        print("¡Gracias por ingresar un número par!")
    else:
        print("Ese no es par. Por favor, ingrese un número par.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

#solicitar edad.
#imprimira categoría perteneciente: 
#niño/a: menor de 12 años.
#adolescente: >=12 años y <18 años.
#adulto/a joven: >=18 años y <30 años.
#adulto/a: >=30 años.

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Categoría: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven")
else:
    print("Categoría: Adulto/a")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

#NOTA: investiguar el uso de la función len()
#para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

#introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
#si ingresa contraseña de longitud adecuada: imprimir mensaje "Ha ingresado una contraseña correcta".
#sino, imprimir: "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

password = ""

# Mientras el largo de la contraseña NO esté entre 8 y 14...
while len(password) < 8 or len(password) > 14:
    password = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
    
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta.")
    else:
        print("Longitud incorrecta. Inténtelo de nuevo.")

print("Registro completado con éxito.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

#programa que tome la lista numeros_aleatorios,
#calcule su moda, su mediana y su media
#compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
#Imprimir resultado.
#Definir la lista numeros_aleatorios de la siguiente forma:
"import random"
"numeros_aleatorios = [random.randint(1, 100) for i in range (50)]"

#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(numeros_aleatorios)
print(f"Moda: {moda}.")
print(f"Mediana: {mediana}.")
print(f"Media: {media}.")

if (media > mediana > moda):
    print("Sesgo Positivo.")
elif (media < mediana < moda):
    print("Sesgo Negativo.")
elif(media == mediana == moda):
    print("Sin Sesgo.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

#solicitar una frase o palabra al usuario.
#si el string ingresado termina con vocal: añadir un signo de exclamación al final.
#sino: dejar el string tal cual lo ingresó el usuaro.

ejecutando = True  # Esta es nuestra "bandera" para el bucle

while ejecutando:
    frase = input("Ingresa una palabra (o escribe 'salir' para terminar): ")

    if frase.lower() == "salir":
        ejecutando = False
        print("Gracias por usar el programa. ¡Hasta pronto!")
    
    elif len(frase) == 0:
        print("No has escrito nada. Intenta de nuevo.")
        
    else:
        ultima_letra = frase[-1]
        vocales = "aiueoAIUEO"

        print(f"Analizando la palabra: '{frase}'...")
        print(f"La última letra es: '{ultima_letra}'")

        if ultima_letra in vocales:
            frase_final = frase + "!"
            print("¡Resultado! Como termina en vocal, añadimos exclamación.")
            print(">>> " + frase_final)
        else:
            print("Resultado: No termina en vocal, se queda igual.")
            print(">>> " + frase)

#quise jugar un poco.

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

#Nota: investigar uso de: upper(), lower() y title()
#para convertir entre mayúsculas y minúsculas.

#solicitar al usuario que ingrese su nombre y el número 1, 2 o 3.
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario.

nombre = input("Ingresa tu nombre: ")
print("¿Con qué formato quiere que se muestre tu nombre?")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Título")

opcion = input("Elige una opción: ")

if opcion == "1":
    print(f"Su nombre se muestra así: {nombre.upper()}")
elif opcion == "2":
    print(f"Su nombre se muestra así: {nombre.lower()}")
elif opcion == "3":
    print(f"Su nombre se muestra así: {nombre.title()}")
else:
    print("Opción no válida")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 9 //////////")
print(" ")

#pedir al usuario la magnitud de un terremoto.
#clasificar la magnitud en una de las siguientes categorías (según la escala de Richter):
#● < 3: "Muy leve" (imperceptible).
#● >= 3 y < 4: "Leve" (ligeramente perceptible).
#● >= 4 y < 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● >= que 5 y < 6: "Fuerte" (puede causar daños en estructuras débiles).
#● >= 6 y < 7: "Muy Fuerte" (puede causar daños significativos).
#● >= 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud del terremoto (Escala Richter): "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif magnitud < 5:
    categoria = "Moderado (sentido por personas, sin daños)"
elif magnitud < 6:
    categoria = "Fuerte (daños en estructuras débiles)"
elif magnitud < 7:
    categoria = "Muy Fuerte (daños significativos)"
else:
    categoria = "Extremo (daños graves a gran escala)"

print(f"El terremoto de magnitud {magnitud} es categorizado como: {categoria}")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 10 //////////")
print(" ")

#Periodo del año            -            norte            -            sur
#---------------------------------------------------------------------------------
#21 de diciembre/20 de marzo            Invierno                      Verano
#21 de marzo/20 de junio               Primavera                      Otoño
#21 de junio/el 20 de septiembre        Verano                       Invierno
#21 de septiembre/20 diciembre           Otoño                       Primavera
#---------------------------------------------------------------------------------
#preguntar al usuario l hemisferio se encuentra (N/S).
#qué mes del año es y qué día es.
#utilizar esa información para imprimir si el usuario se encuentra en:
#otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio donde se encuentra (N/S): ").upper()
mes = int(input("Ingrese el número del mes actual (1-12): "))
dia = int(input("Ingrese el número del día actual: "))

if(1<=dia<=31 and 1<=mes<=12 and (hemisferio == "N" or hemisferio == "S")):
    if(dia>=21 and mes==12) or (mes==1) or (mes==2) or (dia<=20 and mes==3):
        match hemisferio:
            case "N":
                print("Invierno.")
            case "S":
                print("Verano.")

    elif(dia>=21 and mes==3) or (mes==4) or (mes==5) or (dia<=20 and mes==6):
        match hemisferio:
            case "N":
                print("Primavera.")
            case "S":
                print("Otoño.")
    elif(dia>=21 and mes==6) or (mes==7) or (mes==8) or (dia<=20 and mes==9):
        match hemisferio:
            case "N":
                print("Verano.")
            case "S":
                print("Invierno.")
    elif(dia>=21 and mes==9) or (mes==10) or (mes==11) or (dia<=20 and mes==12):
        match hemisferio:
            case "N":
                print("Otoño.")
            case "S":
                print("Primavera.")
else:
    print("Un dato es inválido.")

#fin----------------------------------------------------------------------------------------------------
print("////////// FIN ACTIVIDADES ESTRUCTURAS SECUENCIALES //////////")
