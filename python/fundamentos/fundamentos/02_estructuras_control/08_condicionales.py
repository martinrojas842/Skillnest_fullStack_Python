#Condicionales
#Estructura if - else
num = 15
if num > 20:
   print("Número mayor a 20")
else:
   print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
#Estructura if - elif - else
num = 101
if num > 50:
   print("Número mayor a 50")
elif num > 100:
   print("Número mayor a 100")
else:
   print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
   print("Número menor a 50")

#No se cumple con la condicional, por lo que no se ejecuta el bloque de código

#Tarea desafio
#Ingresar 3 números por tecladoe identificar cual es el mayor y cual es el menor
num1 = int(input("Ingresar primer numero: "))
num2 = int(input("Ingresar segundo numero: "))
num3 = int(input("Ingresar tercer numero: "))

numeros = num1, num2, num3
numMayor = max(numeros)
numMenor = min(numeros)
print(f"Número mayor: {numMayor} \nNúmero menor: {numMenor}")

# Metodo dificil
if num1 > num2 and num1 > num3:
    numMayor = num1
    if num2 > num3:
        numMenor = num3
    else:
        numMenor = num2
elif num2 > num1 and num2 > num3:
    numMayor = num2
    if num1 > num3:
        numMenor = num3
    else:
        numMenor = num1
elif num3 > num1 and num3 > num2:
    numMayor = num3
    if num2 > num1:
        numMenor = num1
    else:
        numMenor = num2
else:
    print("Error")
print(f"Número mayor: {numMayor} \nNúmero menor: {numMenor}")
