print("////////// ACTIVIDAD 1, 2 y 3 //////////")
print(" ")

# ACTIVIDAD 1: Agregar frutas y sus precios

# Creamos el diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregamos las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("ACTIVIDAD 1")
print("Diccionario con las nuevas frutas:")
print(precios_frutas)

# ACTIVIDAD 2: Actualizar los precios

# Modificamos los precios de las frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nACTIVIDAD 2")
print("Diccionario con los precios actualizados:")
print(precios_frutas)

# ACTIVIDAD 3: Crear una lista con las frutas

# Obtenemos los nombres de las frutas
lista_frutas = list(precios_frutas.keys())

print("\nACTIVIDAD 3")
print("Lista de frutas:")
print(lista_frutas)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 4 //////////")
print(" ")

# Agenda de contactos telefónicos

# Creamos un diccionario vacío
contactos = {}

# Pedimos los datos de 5 contactos
for i in range(5):
    nombre = input("\nIngrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")

    # Guardamos el nombre y el teléfono
    contactos[nombre] = telefono

# Buscamos un contacto
buscar = input("\nIngrese el nombre del contacto que desea consultar: ")

if buscar in contactos:
    print("El número de teléfono es:", contactos[buscar])
else:
    print("El contacto no existe.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 5 //////////")
print(" ")

# Contar palabras de una frase

# Pedimos una frase al usuario
frase = input("\nIngrese una frase: ")

# Convertimos la frase en una lista de palabras
palabras = frase.lower().split()

# Creamos un conjunto con las palabras únicas
palabras_unicas = set(palabras)

# Creamos un diccionario para contar las palabras
contador_palabras = {}

# Recorremos las palabras
for palabra in palabras:

    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# Mostramos los resultados
print("Palabras únicas:")
print(palabras_unicas)

print("Cantidad de veces que aparece cada palabra:")
print(contador_palabras)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 6 //////////")
print(" ")

# Promedio de alumnos

# Creamos un diccionario vacío
alumnos = {}

# Pedimos los datos de 3 alumnos
for i in range(3):
    nombre = input("\nIngrese el nombre del alumno: ")

    # Pedimos las tres notas
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    # Guardamos las notas en una tupla
    notas = (nota1, nota2, nota3)

    # Guardamos el alumno y sus notas
    alumnos[nombre] = notas

# Mostramos los promedios
print("Promedios de los alumnos:")

for nombre in alumnos:
    notas = alumnos[nombre]

    promedio = (notas[0] + notas[1] + notas[2]) / 3

    print(nombre, "tiene un promedio de:", round(promedio, 2))

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 7 //////////")
print(" ")

# Alumnos que aprobaron los parciales

# Creamos dos conjuntos de alumnos
parcial1 = {1, 2, 3, 4, 5, 6}
parcial2 = {3, 4, 5, 7, 8, 9}

# Alumnos que aprobaron ambos parciales
ambos = parcial1 & parcial2

# Alumnos que aprobaron solamente uno
solo_uno = parcial1 ^ parcial2

# Alumnos que aprobaron al menos un parcial
total = parcial1 | parcial2

# Mostramos los resultados
print("Alumnos que aprobaron ambos parciales:")
print(ambos)

print("Alumnos que aprobaron solamente un parcial:")
print(solo_uno)

print("Total de alumnos que aprobaron al menos un parcial:")
print(total)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 8 //////////")
print(" ")

# Control de stock de productos

# Creamos un diccionario con algunos productos
stock_productos = {
    'arroz': 10,
    'fideos': 15,
    'leche': 8,
    'huevos': 20
}

# Creamos un menú de opciones
while True:
    print("\nCONTROL DE STOCK")
    print("1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Consultar stock
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")

        if producto in stock_productos:
            print("Stock disponible:", stock_productos[producto])
        else:
            print("El producto no existe.")

    # Agregar unidades
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")

        if producto in stock_productos:
            cantidad = int(input("Ingrese las unidades que desea agregar: "))
            stock_productos[producto] += cantidad
            print("Stock actualizado:", stock_productos[producto])
        else:
            print("El producto no existe.")

    # Agregar un producto nuevo
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")

        if producto not in stock_productos:
            cantidad = int(input("Ingrese la cantidad inicial: "))
            stock_productos[producto] = cantidad
            print("Producto agregado correctamente.")
        else:
            print("El producto ya existe.")

    # Salir del menú
    elif opcion == "4":
        print("Saliendo del control de stock...")
        break

    else:
        print("Opción incorrecta.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 9 //////////")
print(" ")

# Creamos un diccionario con las actividades
agenda = {
    ('Lunes', '08:00'): 'Organización Empresarial',
    ('Martes', '10:00'): 'Comprar',
    ('Miércoles', '17:00'): 'Escuela Rock',
    ('Juevas', '20:00'): 'Jugar Genshin Impact',
    ('Viernes', '01:00'): 'Dormir'
}

# Pedimos el día y la hora que queremos consultar
dia = input("\nIngrese el día: ").capitalize()
hora = input("Ingrese la hora (HH:MM): ")

# Creamos una tupla con el día y la hora
consulta = (dia, hora)

# Consultamos si existe una actividad
if consulta in agenda:
    print("La actividad programada es:", agenda[consulta])
else:
    print("No hay actividades programadas en ese horario.")

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// ACTIVIDAD 10 //////////")
print(" ")

# Invertir un diccionario de países

# Creamos el diccionario original
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Perú': 'Lima'
}

# Creamos un diccionario vacío
capitales_paises = {}

# Recorremos el diccionario original
for pais in paises_capitales:

    # Obtenemos la capital
    capital = paises_capitales[pais]

    # Invertimos las claves y los valores
    capitales_paises[capital] = pais

# Mostramos los resultados
print("Diccionario original:")
print(paises_capitales)

print("\nDiccionario invertido:")
print(capitales_paises)

#fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// FIN ACTIVIDADES FUNCIONES //////////")
