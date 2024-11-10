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

mascotas = [
    {'id': 1, 'nombre': 'Firulais', 'animal': 'Perro', 'raza': 'Labrador', 'lugar_perdido': 'Parque Central', 'fecha_perdida': '2024-11-01', 'info_adicional': 'Llevaba un collar rojo'},
    {'id': 2, 'nombre': 'Michi', 'animal': 'Gato', 'raza': 'Siames', 'lugar_perdido': 'Calle 42', 'fecha_perdida': '2024-10-29', 'info_adicional': 'Es muy tímido'},
    # Add more mascotas as needed
]

@app.route('/test_mascota')
def test_mascota():
    # Mock data for testing the template
    mock_data = {
        'id': 1,
        'nombre': 'Maco',
        'tipo': 'Perro',
        'raza': 'Labrador',
        'descripcion': 'Perro pequeño color marron, encontrado sin collar en Av. Libertador.'
    }
    # Render the template with mock data
    return render_template('perdi_mi_mascota.html', mascota=mock_data)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
