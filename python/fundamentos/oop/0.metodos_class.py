class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

#Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
miyagi.hacer_compra(300)
print(f"Segunda compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
# Imprime cuanto credito le queda a Miyagi
print(f"Credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")

daniel.hacer_compra(45)
print(f"Primera compra de {daniel.nombre}: ${daniel.saldo_pagar}")

16# Imprime cuanto credito le queda a Miyagi
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45

# Tares
"""
1.- Crear un nuevo metodo que permita aumentar el limite de credito.
Imprimir el nuevo limite de credito.

2.- Crear un metodo que permita cambiar el correo de la instancia.
Mostrar el nuevo correo.
"""

miyagi.aumentarCredito(2000)