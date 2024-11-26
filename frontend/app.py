import os
from flask import Flask, flash, render_template, jsonify, request, redirect, url_for
import requests
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
UPLOAD_FOLDER = "static/images"
API_URL = "http://localhost:8080/"

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def homeV1():
    return render_template("homeV1.html")


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


@app.route("/perdi_mi_mascota_filtros")
def perdi_mi_mascota_filtros():
    params = {
        "animal": request.args.getlist("fanimal"),
        "raza": request.args.getlist("fraza"),
        "edad": request.args.getlist("fedad"),
    }
    print(params)
    try:
        response = requests.get(API_URL + "filtro_mascota", params=params)
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
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            imagen_path = f"static/images/{filename}"
        else:
            flash("Archivo no valido.", "error")
            return render_template("encontre_una_mascota.html")

        direccion = request.form.get("fdireccion")
        formulario_data = {
            "nombre": request.form.get("fnombre"),
            "animal": request.form.get("fanimal"),
            "raza": request.form.get("fraza"),
            "color": request.form.get("fcolor"),
            "edad": request.form.get("fedad"),
            "telefono": request.form.get("ftelefono"),
            "email": request.form.get("femail"),
            "fecha": request.form.get("fecha"),
            "descripcion": request.form.get("fmessage"),
            "imagen": imagen_path,
        }

        api_key = "7677b3b3603d4c34bbfc30c063391ca3"  # sin esto no funciona

        if not formulario_data["telefono"].isnumeric():
            flash("Telefono invalido", "error")
            return render_template("encontre_una_mascota.html")

        if not formulario_data["edad"].isnumeric():
            flash("Edad invalida", "error")
            return render_template("encontre_una_mascota.html")

        try:
            url = f"https://api.opencagedata.com/geocode/v1/json?q={direccion}&key={api_key}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["results"]:
                formulario_data["latitud"] = data["results"][0]["geometry"]["lat"]
                formulario_data["longitud"] = data["results"][0]["geometry"]["lng"]

            if not data["results"]:
                flash("No se encontro la dirección ingresada.", "error")
                return render_template("encontre_una_mascota.html")

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener coordenadas: {e}")
            formulario_data["latitud"] = None
            formulario_data["longitud"] = None

        try:
            response = requests.post(API_URL + "crear_mascota", json=formulario_data)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error al enviar los datos a la API: {e}")
            return jsonify({"error": "Hubo un problema al enviar los datos."}), 500

        flash("La mascota se a cargado correctamente.", "success")
        return render_template("encontre_una_mascota.html")

    return render_template("encontre_una_mascota.html")


@app.route("/mascota/<int:mascota_id>")
def mostrar_mascota(mascota_id):
    try:
        response = requests.get(API_URL + f"mascotasPorID/{mascota_id}")
        response.raise_for_status()
        mascota = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return f"Error: {e}", 500

    print(mascota)
    return render_template("mascota_perdida.html", mascota=mascota)


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/eliminarMascota/<int:id>", methods=["GET", "DELETE"])
def eliminarMascota(id):
    try:
        requests.delete(f"{API_URL}/mascotaBorrar/{id}")

    except requests.exceptions.RequestException as e:
        print(f"Error deleting data: {e}")
    return redirect(url_for("perdi_mi_mascota"))


if __name__ == "__main__":
    app.run(debug=True, port=5050)
