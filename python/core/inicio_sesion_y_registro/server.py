from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "esta_es_una_clave_secreta_super_segura"
bcrypt = Bcrypt(app)

# Expresión regular para validar el formato del correo electrónico
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    # Si ya hay sesión iniciada, lo mandamos directo al éxito
    if 'user_id' in session:
        return redirect('/exito')
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    is_valid = True

    # 1. Validar Nombre: solo letras, al menos 2 caracteres
    if len(request.form['nombre']) < 2:
        flash("El nombre debe tener al menos 2 caracteres.", "registro")
        is_valid = False
    elif not request.form['nombre'].isalpha():
        flash("El nombre solo debe contener letras.", "registro")
        is_valid = False

    # 2. Validar Apellido: solo letras, al menos 2 caracteres
    if len(request.form['apellido']) < 2:
        flash("El apellido debe tener al menos 2 caracteres.", "registro")
        is_valid = False
    elif not request.form['apellido'].isalpha():
        flash("El apellido solo debe contener letras.", "registro")
        is_valid = False

    # 3. Validar E-mail: formato correcto y que no exista en la BD
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Formato de correo electrónico inválido.", "registro")
        is_valid = False
    else:
        db = connectToMySQL('login_registro_db')
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': request.form['email']}
        resultado = db.query_db(query, data)
        if len(resultado) > 0:
            flash("El correo electrónico ya está registrado.", "registro")
            is_valid = False

    # 4. Validar Contraseña: al menos 8 caracteres + Bonus Plata (1 mayúscula y 1 número)
    password = request.form['password']
    if len(password) < 8:
        flash("La contraseña debe tener al menos 8 caracteres.", "registro")
        is_valid = False
    elif not re.search(r'[A-Z]', password) or not re.search(r'[0-9]', password):
        flash("La contraseña debe incluir al menos una mayúscula y un número (Bonus Plata).", "registro")
        is_valid = False

    # 5. Confirmación de contraseña
    if password != request.form['confirm_password']:
        flash("Las contraseñas no coinciden.", "registro")
        is_valid = False

    if not is_valid:
        return redirect('/')

    # Hashear la contraseña si todo es válido
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Guardar en la base de datos
    db = connectToMySQL('login_registro_db')
    query = """
        INSERT INTO usuarios (nombre, apellido, email, password) 
        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
    """
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': hashed_password
    }
    user_id = db.query_db(query, data)

    # Guardar ID en sesión
    session['user_id'] = user_id
    session['user_nombre'] = request.form['nombre']

    return redirect('/exito')

@app.route('/login', methods=['POST'])
def login():
    # Buscar el usuario por correo
    db = connectToMySQL('login_registro_db')
    query = "SELECT * FROM usuarios WHERE email = %(email)s;"
    data = {'email': request.form['email']}
    resultado = db.query_db(query, data)

    if len(resultado) == 0:
        flash("Correo electrónico no encontrado.", "login")
        return redirect('/')

    usuario = resultado[0]

    # Verificar la contraseña hasheada
    if not bcrypt.check_password_hash(usuario['password'], request.form['password']):
        flash("Contraseña incorrecta.", "login")
        return redirect('/')

    # Guardar datos en sesión si el login es correcto
    session['user_id'] = usuario['id']
    session['user_nombre'] = usuario['nombre']

    return redirect('/exito')

@app.route('/exito')
def exito():
    # Seguridad: si no hay sesión, no puede entrar aquí
    if 'user_id' not in session:
        flash("Debes iniciar sesión primero.", "login")
        return redirect('/')
    
    return render_template('exito.html', nombre=session['user_nombre'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)