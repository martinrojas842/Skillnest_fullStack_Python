"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
def generadorNiveles():
    for nivel in range(0, 101):
        print(f"Nivel {nivel}")

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
def potenciadoresEnergia():
    for i in range(2, 501, 2):
        print(i)

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
def trampaEmojis():
    for i in range(1, 101):
        if i % 10 == 0:
            print("💣")
        elif i % 5 == 0:
            print("💥")
        else:
            print(i)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
def sumaColosal():
    total = 0
    for i in range(0, 500001, 2):
        total += i
    print(f"Suma total de números pares del 0 al 500,000: {total}")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
def retrocesoTemporal():
    for año in range(2024, -1, -3):
        print(año)

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
def contadorDinamico(inicio, fin, salto):
    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(i)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

continuar = True
while continuar:
    opcion = input("\n--- Elige una opción: (1-6) (0 para salir) --- ")
    if opcion == "0":
        continuar = False
    elif opcion == "1":
        generadorNiveles()
    elif opcion == "2":
        potenciadoresEnergia()
    elif opcion == "3":
        trampaEmojis()
    elif opcion == "4":
        sumaColosal()
    elif opcion == "5":
        retrocesoTemporal()
    elif opcion == "6":
        contadorDinamico(3, 10, 2)