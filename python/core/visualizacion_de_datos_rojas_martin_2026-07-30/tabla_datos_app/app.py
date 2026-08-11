from flask import Flask, render_template

app = Flask(__name__)

datos = [
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "icono": "bi-discord", "color": "#5865F2"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "icono": "bi-instagram", "color": "#E4405F"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "icono": "bi-film", "color": "#E50914"},
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "icono": "bi-spotify", "color": "#1DB954"},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "icono": "bi-tiktok", "color": "#000000"},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "icono": "bi-twitch", "color": "#9146FF"},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "icono": "bi-youtube", "color": "#FF0000"},
]

@app.route("/")
@app.route("/tabla")
@app.route("/rutas")
def mostrar_tabla():
    return render_template("tabla.html", plataformas=datos)

if __name__ == "__main__":
    app.run(debug=True)