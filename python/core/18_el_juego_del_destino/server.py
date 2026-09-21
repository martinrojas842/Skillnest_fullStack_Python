import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

# Clave secreta indispensable para encriptar la sesión en Flask
app.secret_key = "clave_secreta"

# Lista de predicciones (mensajes positivos y de mala suerte)
PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un gran éxito profesional/académico llegará muy pronto a tu vida.",
    "Un viaje inesperado cambiará por completo tu perspectiva.",
    "Cuidado con confiar tus secretos esta semana, podrías tener una decepción.",
    "Hoy no es tu día de suerte: se te caerá algo valioso o tropezarás en público.",
]


# Ruta principal que muestra el formulario para ingresar datos
@app.route("/")
def index():
    return render_template("index.html")


# Ruta para procesar los datos del formulario y almacenarlos en sesión
@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form.get("nombre")
    session["edad"] = request.form.get("edad")
    session["color"] = request.form.get("color")
    session["animal"] = request.form.get("animal")
    return redirect("/futuro")


# Ruta para mostrar la predicción del futuro basada en los datos ingresados
@app.route("/futuro")
def futuro():
    # Validación por si el usuario entra directo a /futuro sin enviar el formulario
    if "nombre" not in session:
        return redirect("/")

    prediccion = random.choice(PREDICCIONES)
    numero_suerte = random.randint(1, 99)

    return render_template(
        "futuro.html",
        nombre=session["nombre"],
        edad=session["edad"],
        color=session["color"],
        animal=session["animal"],
        prediccion=prediccion,
        numero_suerte=numero_suerte,
    )


if __name__ == "__main__":
    app.run(debug=True)