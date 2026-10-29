from flask import Flask
from flask_bcrypt import Bcrypt
from controllers import users

# Inicialización de la aplicación principal
aplicacion = Flask(__name__)
aplicacion.secret_key = 'proyecto_login_seguro_2026_xyz'
bcrypt = Bcrypt(aplicacion)

# --- Mapeo de Rutas del Sistema ---

@aplicacion.route('/')
def inicio():
    return users.index()

@aplicacion.route('/register', methods=['POST'])
def registrar_usuario():
    return users.register(bcrypt)

@aplicacion.route('/login', methods=['POST'])
def iniciar_sesion():
    return users.login(bcrypt)

@aplicacion.route('/dashboard')
def panel_control():
    return users.dashboard()

@aplicacion.route('/logout')
def cerrar_sesion():
    return users.logout()

if __name__ == '__main__':
    aplicacion.run(debug=True, port=5000)