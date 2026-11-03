import sqlite3

print("////////// EJERCICIO 1 //////////")
print(" ")

# Diseñe e implemente las siguientes clases:
# Clase Autor: id_autor, nombre y nacionalidad.
# Clase Libro: id_libro, titulo, anio_publicacion y autor.
# La relación entre Libro y Autor es de agregación.
# Incluir constructores (__init__) y métodos de representación (__str__).

class Autor:

    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre} - Nacionalidad: {self.nacionalidad}"

class Libro:

    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} - Año: {self.anio_publicacion} - Autor: {self.autor.nombre}"

autor1 = Autor(1, "Stephen King", "Estadounidense")
libro1 = Libro(1, "IT (Eso)", 1986, autor1)

print(autor1)
print(libro1)

# fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// EJERCICIO 2 //////////")
print(" ")

# Crear la base de datos biblioteca.db con dos tablas relacionadas:
# Tabla autores: id, nombre y nacionalidad.
# Tabla libros: id, titulo, anio y autor_id.

def inicializar_bd():

    conexion = sqlite3.connect("biblioteca.db")

    cursor = conexion.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nacionalidad TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            anio INTEGER,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")


# fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// EJERCICIO 3 //////////")
print(" ")

# Funciones para gestionar los datos de la biblioteca.

def registrar_autor(nombre, nacionalidad):

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO autores (nombre, nacionalidad)
        VALUES (?, ?)
    """, (nombre, nacionalidad))

    id_autor = cursor.lastrowid

    conexion.commit()
    conexion.close()

    return id_autor

def registrar_libro(titulo, anio, autor_id):

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        INSERT INTO libros (titulo, anio, autor_id)
        VALUES (?, ?, ?)
    """, (titulo, anio, autor_id))

    id_libro = cursor.lastrowid

    conexion.commit()
    conexion.close()

    return id_libro

def listar_libros():

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        ORDER BY libros.id
    """)

    libros = cursor.fetchall()

    for libro in libros:
        print(f"Título: {libro[0]}")
        print(f"Año: {libro[1]}")
        print(f"Autor: {libro[2]}")
        print("------------------------")

    conexion.close()

def actualizar_titulo_libro(id_libro, nuevo_titulo):

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE libros
        SET titulo = ?
        WHERE id = ?
    """, (nuevo_titulo, id_libro))

    conexion.commit()
    conexion.close()

def eliminar_libro(id_libro):

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM libros
        WHERE id = ?
    """, (id_libro,))

    conexion.commit()
    conexion.close()

# fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// EJERCICIO 4 //////////")
print(" ")

# Prueba del funcionamiento completo del sistema:
# 1. Inicializar la base de datos.
# 2. Registrar dos autores y tres libros.
# 3. Listar los libros.
# 4. Actualizar el título de un libro.
# 5. Eliminar un libro y mostrar el listado final.

if __name__ == "__main__":

    # 1. Inicializar la base de datos.
    inicializar_bd()

    print("\nSISTEMA DE GESTION DE BIBLIOTECA")
    print("================================")

    # 2. Registrar dos autores.
    id_autor1 = registrar_autor(
        "Stephen King",
        "Estadounidense"
    )

    id_autor2 = registrar_autor(
        "J.K. Rowling",
        "Britanica"
    )

    # Registrar tres libros.
    id_libro1 = registrar_libro(
        "IT (Eso)", 1986, id_autor1
    )

    id_libro2 = registrar_libro(
        "Carrie", 1974, id_autor1
    )

    id_libro3 = registrar_libro(
        "Harry Potter", 1997, id_autor2
    )

    # 3. Mostrar todos los libros.
    print("\nLISTADO INICIAL DE LIBROS")
    print("=========================")

    listar_libros()

    # 4. Actualizar el título de un libro.
    print("\nACTUALIZACION DE LIBRO")
    print("======================")

    actualizar_titulo_libro(
        id_libro1,
        "IT: El misterio de Pennywise"
    )

    print("Titulo actualizado correctamente.")

    print("\nLISTADO DESPUES DE LA ACTUALIZACION")
    print("===================================")

    listar_libros()

    print("\nELIMINACION DE LIBRO")
    print("====================")

    eliminar_libro(id_libro2)

    print("Libro eliminado correctamente.")

    print("\nLISTADO FINAL DE LIBROS")
    print("=======================")

    listar_libros()

# fin----------------------------------------------------------------------------------------------------
print(" ")
print("////////// FIN ACCESO A DATOS //////////")
