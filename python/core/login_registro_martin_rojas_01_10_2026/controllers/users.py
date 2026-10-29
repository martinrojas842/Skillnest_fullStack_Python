from flask import render_template, request, redirect, session, flash
from models.user import User

def index():
    # Verificación de sesión activa para evitar bucles
    if session.get('user_id'):
        return redirect('/dashboard')
    return render_template('index.html')

def register(bcrypt):
    # Validaciones del modelo mediante lista de errores personalizada
    lista_errores = User.validate_register(request.form)
    
    if lista_errores:
        for err in lista_errores:
            flash(err, 'register_error')
        return redirect('/')

    # Cifrado de contraseña con un nombre de variable propio
    clave_cifrada = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    
    datos_nuevo_usuario = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': clave_cifrada,
        'birthday': request.form['birthday']
    }

    # Registro en la base de datos y apertura de sesión
    nuevo_id = User.save(datos_nuevo_usuario)
    session['user_id'] = nuevo_id
    
    flash("¡Cuenta creada exitosamente!", "success")
    return redirect('/dashboard')

def login(bcrypt):
    # Extracción segura de credenciales
    correo_ingresado = request.form.get('email', '')
    pass_ingresada = request.form.get('password', '')
    
    usuario_encontrado = User.get_by_email(correo_ingresado)
    
    if not usuario_encontrado or not bcrypt.check_password_hash(usuario_encontrado.password, pass_ingresada):
        flash("Datos incorrectos. Verifica tu correo y contraseña.", 'login_error')
        return redirect('/')

    # Establecer sesión tras validación exitosa
    session['user_id'] = usuario_encontrado.id
    return redirect('/dashboard')

def dashboard():
    # Control de acceso seguro al panel
    if 'user_id' not in session:
        flash("Acceso denegado. Por favor inicia sesión primero.", "login_error")
        return redirect('/')
    
    usuario_actual = User.get_by_id(session['user_id'])
    return render_template('dashboard.html', user=usuario_actual)

def logout():
    # Limpieza total de sesión
    session.clear()
    return redirect('/')