datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(datos)
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def carlos(lista):
    for nombres in lista:
        if nombres["nombre"] == "Carlos":
            print(f"{nombres["nombre"]} obtuvo {nombres["puntaje"]} puntos.")

carlos(datos)

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

def recibirNombre(lista):
    opcion = input("Nombre o puntaje?:")
    if opcion == "Nombre":
        print("Nombres almacenados: ")
        for nombres in lista:
            print(nombres["nombre"])
    elif opcion == "Puntaje":
                print("Puntajes almacenados:")
                for puntajes in lista:
                    print(puntajes["puntaje"])
    else:
        print("Ingrese un valor válido")

recibirNombre(datos)