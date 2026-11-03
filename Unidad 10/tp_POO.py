print(" Ejercicio 1: Celda y Matriz. ")

class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila          # entero
        self.columna = columna    # entero
        self.valor = valor        # cadena

class Matriz:
    def __init__(self):
        self.celdas = []          

    def existeCelda(self, fila, columna):
        """Devuelve True si ya hay una celda cargada con esa fila y columna."""
        for celda in self.celdas:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    def agregarCelda(self, celda):
        self.celdas.append(celda)

    def mostrarCeldas(self):
        print("\n--- Celdas cargadas ---")
        for celda in self.celdas:
            print(f"Fila: {celda.fila} | Columna: {celda.columna} | Valor: {celda.valor}")

    def obtenerValor(self, fila, columna):
        """Devuelve el valor de la celda indicada o un mensaje si no existe."""
        for celda in self.celdas:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

def leerEntero(mensaje):
    """Pide un número entero y repite hasta que el usuario escriba uno válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")

def main():
    matriz = Matriz()

    while True:
        valor = input("\nIngrese el valor de la celda (FIN para terminar): ")
        if valor.upper() == "FIN":
            break

        fila = leerEntero("Ingrese la fila: ")
        columna = leerEntero("Ingrese la columna: ")

        if matriz.existeCelda(fila, columna):
            print("Esa fila y columna ya fueron cargadas. No se guardó el valor.")
        else:
            matriz.agregarCelda(Celda(fila, columna, valor))
            print("Celda guardada.")

    matriz.mostrarCeldas()

    print("\n--- Consulta de una celda ---")
    fila = leerEntero("Fila a consultar: ")
    columna = leerEntero("Columna a consultar: ")
    print("Valor:", matriz.obtenerValor(fila, columna))

if __name__ == "__main__":
    main()

#fin--------------------------------------------------------------------------------------------

print(" ")
print(" Ejercicio 2: Carga de notas de alumnos. ")

class Nota:
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra          # cadena
        self.notaExamen = notaExamen    # decimal

class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto   # cadena
        self.legajo = legajo                   # entero
        self.notas = []                        # lista de objetos Nota

    def agregarNota(self, nota):
        self.notas.append(nota)

    def calcularPromedio(self):
        """Suma todas las notas y divide por la cantidad de notas."""
        if len(self.notas) == 0:
            return 0
        total = 0
        for nota in self.notas:
            total += nota.notaExamen
        return total / len(self.notas)

    def mostrar(self):
        print(f"Alumno: {self.nombreCompleto} (Legajo {self.legajo})")
        for nota in self.notas:
            print(f"   Cátedra: {nota.catedra} - Nota: {nota.notaExamen}")
        print(f"   El promedio del alumno es: {self.calcularPromedio():.2f}")

def leerEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")

def leerNota(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 10:
                return valor
            print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Debe ingresar un número (ejemplo: 7.5).")

def leerSiNo(mensaje):
    """Devuelve True si el usuario escribe SI y False si escribe NO."""
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "SI":
            return True
        if respuesta == "NO":
            return False
        print("Responda SI o NO.")

class CargaNotas:
    @staticmethod
    def main():
        alumnos = []

        while True:
            print("\nINGRESE DATOS DEL ALUMNO")
            nombre = input("Nombre completo: ")
            legajo = leerEntero("Legajo: ")
            alumno = Alumno(nombre, legajo)
            
            while True:
                catedra = input("Nombre de la cátedra: ")
                nota = leerNota("Nota: ")
                alumno.agregarNota(Nota(catedra, nota))
                if not leerSiNo("¿Desea cargar otra nota? (SI/NO): "):
                    break

            alumnos.append(alumno)

            if not leerSiNo("¿Desea cargar otro alumno? (SI/NO): "):
                break

        print("\n========== DATOS CARGADOS ==========")
        for alumno in alumnos:
            alumno.mostrar()
            print("====================================")

if __name__ == "__main__":
    CargaNotas.main()

#fin--------------------------------------------------------------------------------------------

print(" Ejercicio 3: Menu de Restaurante. ")

class Ingrediente:
    def __init__(self, nombre, cantidad, unidadMedida):
        self.nombre = nombre                # cadena
        self.cantidad = cantidad            # decimal
        self.unidadMedida = unidadMedida    # cadena

def formato(numero):
    """Muestra 450.0 como 450 y 12.5 como 12.50."""
    if numero == int(numero):
        return str(int(numero))
    return f"{numero:.2f}"

class Plato:
    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto   # cadena
        self.precio = precio                   # decimal
        self.esBebida = esBebida               # booleano
        self.ingredientes = []                 # lista de objetos Ingrediente

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def mostrar(self):
        print(self.nombreCompleto)
        print(f"Precio: $ {formato(self.precio)}")
        if not self.esBebida:
            print("Ingredientes:")
            print(f"{'Nombre':<20}{'Cantidad':<10}Unidad de Medida")
            for ing in self.ingredientes:
                print(f"{ing.nombre:<20}{formato(ing.cantidad):<10}{ing.unidadMedida}")

def leerDecimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un número.")

def leerSiNo(mensaje):
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "SI":
            return True
        if respuesta == "NO":
            return False
        print("Responda SI o NO.")

class MenuRestaurante:
    @staticmethod
    def main():
        platosMenu = []

        while True:
            print("\n--- Nuevo plato ---")
            nombre = input("Nombre del plato: ")
            precio = leerDecimal("Precio: ")
            esBebida = leerSiNo("¿Es una bebida? (SI/NO): ")
            plato = Plato(nombre, precio, esBebida)

            # Solo si no es bebida se piden ingredientes 
            if not esBebida:
                while True:
                    nombreIng = input("  Nombre del ingrediente: ")
                    cantidad = leerDecimal("  Cantidad: ")
                    unidad = input("  Unidad de medida (gramos, unidades...): ")
                    plato.agregarIngrediente(Ingrediente(nombreIng, cantidad, unidad))
                    if not leerSiNo("  ¿Desea agregar otro ingrediente? (SI/NO): "):
                        break

            platosMenu.append(plato)

            if not leerSiNo("¿Desea cargar otro plato? (SI/NO): "):
                break

        print("\n-----------MENÚ----------------")
        for plato in platosMenu:
            plato.mostrar()
            print("----------------------------------")

if __name__ == "__main__":
    MenuRestaurante.main()

#fin--------------------------------------------------------------------------------------------

print(" ")
print(" Ejercicio 4: Carga de productos de supermercado. ")

class ComponenteCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente   # cadena
        self.marca = marca             # cadena
        self.cantidad = cantidad       # entero
        self.precio = precio           # decimal 

    def calcularSubtotal(self):
        return self.precio * self.cantidad

def formato(numero):
    """Muestra 59500.0 como 59500 y 123.456 como 123.46."""
    if numero == int(numero):
        return str(int(numero))
    return f"{numero:.2f}"

class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca                # cadena
        self.modelo = modelo              # cadena
        self.componentes = []             # lista de objetos ComponenteCPU

    def agregarComponente(self, componente):
        self.componentes.append(componente)

    def calcularCosto(self):
        """Suma el subtotal (precio x cantidad) de cada componente."""
        total = 0
        for componente in self.componentes:
            total += componente.calcularSubtotal()
        return total

    def calcularGanancia(self):
        """40% del costo si el costo es menor a 50000; si no, 30%."""
        costo = self.calcularCosto()
        if costo < 50000:
            return costo * 0.40
        return costo * 0.30

    def calcularPrecioVenta(self):
        return self.calcularCosto() + self.calcularGanancia()

    def mostrar(self):
        print("\n-----------Computadora----------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes:")
        print(f"{'Componente':<20}{'Marca':<12}{'Cantidad':<10}{'Precio X Unidad':<17}SubTotal")
        for c in self.componentes:
            print(f"{c.componente:<20}{c.marca:<12}{c.cantidad:<10}"
                  f"{formato(c.precio):<17}{formato(c.calcularSubtotal())}")
        costo = self.calcularCosto()
        print(f"Costo Total {formato(costo)}")
        print(f"El precio sugerido de venta es {formato(costo)} + "
              f"{formato(self.calcularGanancia())} = {formato(self.calcularPrecioVenta())}")

def leerEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un número mayor a 0.")
        except ValueError:
            print("Debe ingresar un número entero.")

def leerDecimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un número mayor a 0.")
        except ValueError:
            print("Debe ingresar un número.")

def leerSiNo(mensaje):
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "SI":
            return True
        if respuesta == "NO":
            return False
        print("Responda SI o NO.")

class CostoComputadora:
    @staticmethod
    def main():
        while True:     # cada vuelta cotiza una computadora nueva
            marca = input("\nMarca de la computadora: ")
            modelo = input("Modelo: ")
            compu = Computadora(marca, modelo)

            while True:
                print("--- Nuevo componente ---")
                nombre = input("Componente: ")
                marcaComp = input("Marca: ")
                cantidad = leerEntero("Cantidad: ")
                precio = leerDecimal("Precio por unidad: ")
                compu.agregarComponente(ComponenteCPU(nombre, marcaComp, cantidad, precio))
                if not leerSiNo("¿Desea agregar otro componente? (SI/NO): "):
                    break

            compu.mostrar()

            if not leerSiNo("\n¿Desea cotizar una nueva computadora? (SI/NO): "):
                break

        print("Fin del programa.")

if __name__ == "__main__":
    CostoComputadora.main()

#fin--------------------------------------------------------------------------------------------

print(" ")
print(" Ejercicio 5: Barrio, Vivienda y Habitaciones. ")
print(" ")

class Habitacion:
    def __init__(self, nombre, metrosCuadrados):
        self.nombre = nombre                      # cadena.
        self.metrosCuadrados = metrosCuadrados    # decimal.

class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle                          # cadena.
        self.numero = numero                        # entero.
        self.manzana = manzana                      # cadena.
        self.nroCasa = nroCasa                      # entero.
        self.superficieTerreno = superficieTerreno  # decimal.
        self.habitaciones = []                      # lista de objetos Habitacion.

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total = 0
        for habitacion in self.habitaciones:
            total += habitacion.metrosCuadrados

        if total > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")

        return total

class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre                            # cadena.
        self.empresaConstructora = empresaConstructora  # cadena.
        self.viviendas = []                             # lista de objetos Vivienda.

    def agregarVivienda(self, vivienda):
        self.viviendas.append(vivienda)

    # a) suma el terreno de todas las viviendas.
    def getSuperficieTotalTerreno(self):
        total = 0
        for vivienda in self.viviendas:
            total += vivienda.superficieTerreno
        return total

    # b) suma el terreno solo de las viviendas de una manzana.
    def getSuperficieTotalTerrenoXManzana(self, manzana):
        total = 0
        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                total += vivienda.superficieTerreno
        return total

    # d) suma los metros cubiertos reutilizando el método de Vivienda.
    def getSuperficieTotalCubierta(self):
        total = 0
        for vivienda in self.viviendas:
            total += vivienda.getMetrosCuadradosCubiertos()
        return total

def main():
    barrio = Barrio("Los Álamos", "Constructora Sur")

    # Vivienda 1 (manzana A): terreno 200 m2, cubierto 40 + 15 + 12 = 67 m2.
    v1 = Vivienda("San Martín", 120, "A", 1, 200)
    v1.agregarHabitacion(Habitacion("Living", 40))
    v1.agregarHabitacion(Habitacion("Dormitorio", 15))
    v1.agregarHabitacion(Habitacion("Baño", 12))

    # Vivienda 2 (manzana A): terreno 250 m2, cubierto 50 + 20 = 70 m2.
    v2 = Vivienda("San Martín", 130, "A", 2, 250)
    v2.agregarHabitacion(Habitacion("Living", 50))
    v2.agregarHabitacion(Habitacion("Dormitorio", 20))

    # Vivienda 3 (manzana B): terreno 300 m2, cubierto 60 + 25 + 10 = 95 m2.
    v3 = Vivienda("Belgrano", 45, "B", 3, 300)
    v3.agregarHabitacion(Habitacion("Living", 60))
    v3.agregarHabitacion(Habitacion("Dormitorio", 25))
    v3.agregarHabitacion(Habitacion("Baño", 10))

    barrio.agregarVivienda(v1)
    barrio.agregarVivienda(v2)
    barrio.agregarVivienda(v3)

    print(f"Barrio: {barrio.nombre} - Constructora: {barrio.empresaConstructora}")
    print("Superficie total de terreno:", barrio.getSuperficieTotalTerreno(), "m2")
    print("Superficie de terreno manzana A:", barrio.getSuperficieTotalTerrenoXManzana("A"), "m2")
    print("Superficie de terreno manzana B:", barrio.getSuperficieTotalTerrenoXManzana("B"), "m2")
    print("Metros cubiertos de la vivienda 1:", v1.getMetrosCuadradosCubiertos(), "m2")
    print("Superficie total cubierta del barrio:", barrio.getSuperficieTotalCubierta(), "m2")

    # Prueba de la excepción: una casa con más metros cubiertos que terreno.
    print("\n--- Prueba de la excepción ---")
    vInvalida = Vivienda("Mitre", 10, "C", 4, 50)
    vInvalida.agregarHabitacion(Habitacion("Salón", 40))
    vInvalida.agregarHabitacion(Habitacion("Dormitorio", 30))
    try:
        vInvalida.getMetrosCuadradosCubiertos()
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()

#fin--------------------------------------------------------------------------------------------

print(" ")
print("/// Fin Actividades POO ///")
print(" ")