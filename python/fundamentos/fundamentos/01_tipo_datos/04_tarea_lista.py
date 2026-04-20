"""
Actividad: Gestor de inventario
"""

"""
1.- Creacion: Crear una lista llamada inventario que contenga los siguientes articulos:
"laptop", "Raton", "Monitor", "Cable hdmi".
"""
inventario = ["laptop", "raton", "monitor", "cable hdmi"]
"""
2.- Expansion: Utiliza el metodo correspondiente para agregar "Impresora" y "teclado" al final de la lista.
"""
inventario.append("impresora")
inventario.append("teclado")
"""
3.- Conteo: Utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista.
"""
print(len(inventario))
"""
4.- Acceso y modificacion: Modifica "Teclado" por "Teclado mecanico".
"""
inventario[5] = "teclado mecanico"
"""
5.- Slicing: Crea una nueva lista llamada "promocion", 
debe contener solo los 3 primeros elementos de la< lista "inventario".
"""
promocion = inventario[:3]
print(promocion)
"""
6.- Mostrar la lista de inventario ordenado alfabeticamente.
"""
inventario.sort()
print(inventario)
"""
7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final
"""
elemento_eliminado = inventario.pop()
print(elemento_eliminado)