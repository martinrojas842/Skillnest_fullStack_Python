from config.connection import connectToMySQL
import re
from datetime import datetime, date

PATRON_CORREO = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PATRON_NOMBRE = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')
PATRON_CLAVE = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')

class User:
    def __init__(self, datos_fila):
        self.id = datos_fila['id']
        self.first_name = datos_fila['first_name']
        self.last_name = datos_fila['last_name']
        self.email = datos_fila['email']
        self.password = datos_fila['password']
        self.birthday = datos_fila['birthday']
        self.created_at = datos_fila['created_at']
        self.updated_at = datos_fila['updated_at']

    @classmethod
    def save(cls, dict_datos):
        sql_insert = "INSERT INTO users (first_name, last_name, email, password, birthday) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(birthday)s);"
        return connectToMySQL().query_db(sql_insert, dict_datos)

    @classmethod
    def get_by_email(cls, correo):
        sql_consulta = "SELECT * FROM users WHERE email = %(email)s;"
        resultados = connectToMySQL().query_db(sql_consulta, {'email': correo})
        return cls(resultados[0]) if resultados else None

    @classmethod
    def get_by_id(cls, identificador):
        sql_consulta = "SELECT * FROM users WHERE id = %(id)s;"
        resultados = connectToMySQL().query_db(sql_consulta, {'id': identificador})
        return cls(resultados[0]) if resultados else None

    @staticmethod
    def validate_register(dict_datos):
        lista_errores = []
        
        # Validar Nombre
        nombre = dict_datos.get('first_name', '').strip()
        if len(nombre) < 2:
            lista_errores.append("El nombre debe poseer como mínimo 2 caracteres.")
        elif not PATRON_NOMBRE.match(nombre):
            lista_errores.append("El campo nombre solo admite caracteres alfabéticos.")

        # Validar Apellido
        apellido = dict_datos.get('last_name', '').strip()
        if len(apellido) < 2:
            lista_errores.append("El apellido debe poseer como mínimo 2 caracteres.")
        elif not PATRON_NOMBRE.match(apellido):
            lista_errores.append("El campo apellido solo admite caracteres alfabéticos.")

        # Validar Email
        correo = dict_datos.get('email', '').strip()
        if not PATRON_CORREO.match(correo):
            lista_errores.append("El formato del correo electrónico ingresado no es válido.")
        elif User.get_by_email(correo):
            lista_errores.append("Este correo ya se encuentra registrado en el sistema.")

        # Validar Fecha de Nacimiento (Mayor de 18 años)
        texto_cumple = dict_datos.get('birthday', '')
        if not texto_cumple:
            lista_errores.append("Es obligatorio ingresar la fecha de nacimiento.")
        else:
            try:
                fecha_nac = datetime.strptime(texto_cumple, '%Y-%m-%d').date()
                fecha_actual = date.today()
                calculo_edad = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))
                if calculo_edad < 18:
                    lista_errores.append("Debes ser mayor de edad (+18) para completar el registro.")
            except ValueError:
                lista_errores.append("La estructura de la fecha de nacimiento no es correcta.")

        # Validar Contraseña
        clave = dict_datos.get('password', '')
        if len(clave) < 8:
            lista_errores.append("La contraseña necesita tener al menos 8 caracteres.")
        elif not PATRON_CLAVE.match(clave):
            lista_errores.append("La contraseña debe incluir obligatoriamente un número y una letra mayúscula.")

        # Confirmación de contraseña
        if clave != dict_datos.get('confirm_password', ''):
            lista_errores.append("Las contraseñas proporcionadas no coinciden.")

        return lista_errores