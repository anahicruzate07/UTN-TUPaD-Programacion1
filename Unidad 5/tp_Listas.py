print("////////// ACTIVIDAD 1 //////////")
print(" ")

#Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
#Utilizar la función range.

multiplos = list(range(4, 101, 4))
print(multiplos)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 2 //////////")
print(" ")

#lista con cinco elementos, mostrar el penúltimo.

lista = ["Pokemon", "Spore", "Minecraf", "Genshin Impact", "GTA SA"]
print(lista)
print(lista[-2])

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 3 //////////")
print(" ")

#Crear una lista vacía, agregar tres palabras con append,
#imprimir la lista resultante por pantalla.

lista_vacia = []

lista_vacia.append("Hu Tao")
lista_vacia.append("Arcanine")
lista_vacia.append("Pyro")

print(lista_vacia)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

#Reemplazar el segundo y último valor de la lista “animales”
#con las palabras “loro” y “oso”, respectivamente.
#Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]
print(animales)

animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)

#1- Crea una lista de numeros.
#2- Busca el numero mas grande usando max().
#3- Elimina ese numero grande usando .remove().
#4- Muestra pos pantalla la lista con el numero ya eliminado.

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

#Crear una lista con números del 10 al 30 (incluído),
# haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros = list(range(10, 31, 5))

print(numeros[:2])

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
# por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
print(autos)

autos[1] = "BMX"
autos[2] = "limusina"
print(autos)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

#lista vacía llamada "dobles"
#agregar el doble de 5, 10 y 15 usando append.

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 9 //////////")
print(" ")

#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(compras)

#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

#d) Imprimir la lista resultante por pantalla
print(compras)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 10 //////////")
print(" ")

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

#fin----------------------------------------------------------------------------------------------------
print("////////// FIN ACTIVIDADES LISTAS //////////")
