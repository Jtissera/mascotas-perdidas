from flask import Flask, render_template
import requests

API_URL = 'http://localhost:8080/'
app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/perdi_mi_mascota")
def perdi_mi_mascota():
    try:
        response = requests.get(API_URL + 'mascotas')
        response.raise_for_status()
        mascotas = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        mascotas = []

    return render_template("perdi_mi_mascota.html", mascotas=mascotas)


@app.route("/encontre_una_mascota")
def encontre_una_mascota():
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
