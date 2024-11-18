import os
from flask import Flask, render_template, jsonify, request
import requests
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
UPLOAD_FOLDER = "static/images"
API_URL = "http://localhost:8080/"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/perdi_mi_mascota")
def perdi_mi_mascota():
    mascotas_info = request.args.get("fsearch")
    params = {"filtro": mascotas_info}

    try:
        response = requests.get(API_URL + "mascotas", params=params)
        response.raise_for_status()
        mascotas = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        mascotas = []

    return render_template("perdi_mi_mascota.html", mascotas=mascotas)


@app.route("/encontre_una_mascota", methods=["GET", "POST"])
def encontre_una_mascota():
    if request.method == "POST":
        file = request.files["fimage"]
        formulario_data = {
            "nombre": request.form.get("fnombre"),
            "animal": request.form.get("fanimal"),
            "raza": request.form.get("fraza"),
            "color": request.form.get("fcolor"),
            "edad": request.form.get("fedad"),
            "zona": request.form.get("fzona"),
            "telefono": request.form.get("ftelefono"),
            "email": request.form.get("femail"),
            "fecha": request.form.get("fecha"),
            "descripcion": request.form.get("fmessage"),
            "imagen": f"static/images/{file.filename}",
        }

        try:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            response = requests.post(API_URL + "crear_mascota", json=formulario_data)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error al enviar los datos a la API: {e}")
            return jsonify({"error": "Hubo un problema al enviar los datos."}), 500

        return render_template("homeV1.html")

    return render_template("encontre_una_mascota.html")


@app.route("/")
def homeV1():
    return render_template("homeV1.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
