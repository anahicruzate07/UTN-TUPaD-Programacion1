print("////////// PRÁCTICA ARCHIVOS //////////")
print(" ")

# PUNTO 1: Crear archivo inicial con productos

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,850.0,15\n")
    archivo.write("Goma,75.0,20\n")

# PUNTO 2: Leer y mostrar productos

print("LISTA DE PRODUCTOS")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")

        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]

        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# PUNTO 3: Agregar productos desde teclado

print("\nAGREGAR PRODUCTO")

nombre = input("Ingrese el nombre: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

# PUNTO 4: Cargar productos en una lista de diccionarios

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")

        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }

        productos.append(producto)

# PUNTO 5: Buscar producto por nombre

print("\nBUSCAR PRODUCTO")

nombre_buscar = input("Ingrese el nombre del producto: ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print("Producto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")

        encontrado = True

if encontrado == False:
    print("Error: el producto no existe.")

# PUNTO 6: Guardar los productos actualizados

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(
            f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        )

print("\nArchivo actualizado correctamente.")

print(" ")
print("////////// FIN PRÁCTICA ARCHIVOS //////////")

# ¿Se puede agregar más de un producto?:
# No, ya que en el punto 3 pide agregar un solo producto, no más.

# ¿Se guarda todo correctamente?
# No, ya que el punto 1 utiliza el modo 'w', que borra el contenido anterior 
#cada vez que se ejecuta el programa.