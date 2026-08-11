# EJERCICIOS
"""1.-Crear una función que reciba una lista de números enterosy muestre cuál es el número
mayor y cuál es el menor."""
def listaNumeros(listado):
    menor = min(listado)
    mayor = max(listado)


ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit}: "))
        listNum.append(num)
        i += 1
    numeroMayorMenos(listaNumeros)

"""2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene."""
def es_vocal(letra):
    vocales = "aeiuoAEIOU"
    return letra in vocales #Devuelve True si la letra está dentro de las vocales, si 
    
def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales.")

def ejercicio_contar_vocales():
    texto = input("Ingrese el texto: ")



"""3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que
tengan más de 5 letras."""
def filtrar(lista)
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def mostrar():
    nombres = []
    nombresLargos = []
    cantidad = int(input("¿Cuántos nombres quieres ingresar?: "))

    for i in range(cantidad)
    nombre = input("Ingrese un nombre: ")
    print(f"{nombre} agregado con éxito a la lista.")
    nombres.append(nombre)

    listaNombres = filtrar(nombres)
    print(f"Los nombres con más de 5 letras son: \n- {("\n-").join(listaNombres)}")

mostrar()
"""4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio
e indique si el estudiante aprueba (promedio mayor o igual a 4.0)."""
def calcularPromedio(nota):
    promedio = sum(notas)/ len(notas)
    print(f"Promedio general del estudiante: {promedio}")
    return promedio

def aprobadoReprobado(promedio, nombre):
    if promedio >= 4.0:
        print(f"El estudiante {nombre} aprobó con un promedio general de {promedio}")
    elif promedio < 4.0:
        print(f"El estudiante {nombre} reprobó con un promedio general de {promedio}")
    else:
        print("Error")

def recibirNotas()
    estudiante = input("Ingrese el nombre del estudiante:")
    cantidad = input("Ingrese la cantidad de notas a ingresar: ")
    listaNotas = []
    for i in range(cantidad)
        nota = float(input(f"Ingrese la nota N°{i + 1} de {estudiante}"))
        listaNotas.append(nota)
    promedioFinal = calcularPromedio(listaNotas)
    aprobadoReprobado(promedioFinal, estudiante)

recibirNotas()
"""5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del
10%, mostrando el valor original y el nuevo valor."""
def descuento(valor)
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento =sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es: \n{precioFinal}\ny con descuento \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiera \n"))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor de el producto \n"))
        listaPrecios.append(valorProducto)
    descuento(listaPrecios)
valores()

"""6.-Crear una función que reciba un número entero y determine si es par o impar."""
def numeroEntero()

""""7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores
de edad (18 años o más)."""
def listaEdades()

"""8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece
una palabra específica ingresada por el usuario."""
def listaPalabras()

"""9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga
únicamente los números positivos."""
def listaPositivos()


"""10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre
y stock) y muestre cuáles tienen un stock menor a 5 unidades."""
def productosDiccionario()


def limpiar_consola():
    os.system('cls')

