# Pasar argumentos
"""Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al metodo __init__
y que de esta manera podamos asignarle a los atributos los valores correspondientes."""

class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

# Creacion de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 40000, 20000)
martin = Usuario("Martin", "Rojas", "martinrojas@liceovvh.cl", 50000, 30000)
# Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(martin.nombre) # Imprime: Martin

# Tarea
"""
Crea una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crea 3 instancias para la clase con distintos estudiantes.
- Imprime el nombre y el apellido concatenado + especialidad.
"""
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac)
    self.rut = rut
    self.nombre = nombres
    self.apellido = apellido
    self.especialidad = especialidad
    self.fecha_nac = fecha_nac

# Creacion de las instancias
isidora = Estudiante("22796812-5", "Isidora", "Valenzuela", "Programacion", "19-06-2008")
arael = Estudiante("23036981-k", "Arael", "Anabalon", "Programacion", "06-06-2009")
yuli = Estudiante("27461998-8", "Yulieth", "Gonzalez", "Programacion", "12-03-2008")