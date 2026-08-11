"""
05. Atributos, Métodos y Clases
"""
# Definición de la clase:
class Estudiante:
    colegio = "Liceo comercial Vate Vicente Huidobro" # <-- Atributo de clase
    alumnos = [] # <-- Lista en donde están todos los estudiantes

    # Método constructor:
    def __init__(self, nombre, nota):
        # Atributos de instancia:
        self.nombre = nombre
        self.nota = nota

# Agregar elementos a la lista "alumnos:
Estudiante.alumnos.append(self)

# Metodo de instancia:
def mostrarInfo(self):
    print(f"Nombre: (self.nombre)\nNota: (self.nota)")

# Metodo de CLASE
# Usa "cls" porque trabaja con la informacion de la clase
@classmethod:
def cambiar_colegio(cls, nuevo_nombre):
    cls.colegio = nuevo_nombre

@classmethod # Contar la cantidad de estudiantes existentes.
def cantidad_estudiantes(cls):
    return len(cls.estudiantes)

# Metodo estatico
# Este no usa CLS ni SELF; solo parametros.
@staticmethod
def aprobar(nota):
    if nota >= 4.0:
        return True
    else:
        return False

# Creacion de objetos(Instancias)
estudiantes = Estudiante("Donovan", 4.0)
estudiantes = Estudiante("Randy", 6.7)

# Uso de metodos de instancias
print("== METODO DE INSTANCIA==")
# Mostrar datos de estudiantes
e1_mostrar_info()
print()
e2_mostrar_info()
print()

# Usar atributos de clase
print("===ATRIBUTO DE CLASE===")
print(e1.colegio)
print(e2.colegio)

Estudiante.cambiar_colegio("Purkuyen")
print(e1.colegio)
print(e2.colegio)
print()

# Contar estudiantes
print("===CONTAR ESTUDIANTES===")
print(f"Total estudiantes: {Estudiante.candidad_estudiantes()}")
# Función de repaso:
def validadorDatos(usuario, contrasena):
    if usuario == "Matias123" and contrasena == "matias123":
        print(f"Bienvenido usuario {usuario}!")
        return True
    else:
        print("Acceso denegado...")
        return False

def ingresarDatos():
    user = input("Ingrese nombre de Usuario: ")
    password = input(f"Ingrese la contraseña de {user}")
    validador = validadorDatos(user, password)
ingresarDatos()