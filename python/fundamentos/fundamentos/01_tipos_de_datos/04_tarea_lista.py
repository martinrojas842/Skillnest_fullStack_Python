'''
Actividad: Gestor de inventario.
'''

''' #1.- Creación: Crear una lista llamada inventario que contenga los siguientes
# Articulos: "Laptop", "ratón", "monitor", "cable hdmi" '''

inventario = ['Laptop', 'ratón', 'monitor', 'cable hdmi',]

''' 2.- Expansión: Utiliza el método correspondiente para agregar "impresora" y "teclado"
al final de la lista. '''

inventario.append("impresora")
inventario.append("teclado")

'''3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos
totales hay en la lista. '''

print(len(inventario))

''' 4.- Acceso y modificación: Modifica "teclado" por "teclado mecánico" '''

inventario[4] = "teclado mecanico"

''' 5.- Slicing: Crea una nueva lista llamada "promoción", debe contener
solo los 3 primeros elementos de la lista "inventario". '''

promocion = inventario[:3]

''' 6.- Mostrar la lista de inventario ordenado alfabeticamente. '''

inventario.sort()
print(inventario)

''' 7.- Elimina el último elemento de la lista inventario mostrando el elemento
eliminado y la lista final. ''' 

elemento_eliminado = inventario.pop()
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Lista final: {inventario}")