from flask import Flask, render_template, request

app = Flask(__name__)

estudiantes_lista = [
    {"nombre": "Ana Pérez", "carrera": "Ingeniería de Sistemas", "semestre": 3},
    {"nombre": "Luis Gómez", "carrera": "Ingeniería Industrial", "semestre": 5},
    {"nombre": "María Torres", "carrera": "Ingeniería de Software", "semestre": 2},
]

@app.route("/")
def inicio():
    return render_template("inicio.html", titulo="Inicio")

@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html", titulo="Estudiantes", estudiantes=estudiantes_lista)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    mensaje_enviado = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        mensaje_enviado = f"Gracias {nombre}, tu mensaje fue recibido."
    return render_template("contacto.html", titulo="Contacto", mensaje_enviado=mensaje_enviado)



if __name__ == "__main__":
    app.run(debug=True)
