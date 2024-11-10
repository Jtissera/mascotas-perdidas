from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/perdi_mi_mascota")
def perdi_mi_mascota():
    return render_template("perdi_mi_mascota.html")


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

@app.route('/mascota/<int:mascota_id>')
def mostrar_mascota(mascota_id):
    mascota = obtener_mascota_por_id(mascota_id)  # Una función que busca la mascota por ID
    return render_template('mascota_perdida.html', mascota=mascota)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
