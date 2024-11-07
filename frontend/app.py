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

if __name__ == "__main__":
    app.run(debug=True, port=5050)
