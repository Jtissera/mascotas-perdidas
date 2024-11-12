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

def obtener_mascota_por_id(mascota_id):
    # Search for the pet in the in-memory list
    for mascota in mascotas:
        if mascota['id'] == mascota_id:
            return mascota
    return None  # Return None if no matching pet is found

@app.route('/mascota/<int:mascota_id>')
def mostrar_mascota(mascota_id):
    mascota = obtener_mascota_por_id(mascota_id)  # Una función que busca la mascota por ID
    return render_template('mascota_perdida.html', mascota=mascota)

mascotas = [
    {
        'id': 1,
        'nombre': '#N/A',
        'animal': 'Perro',
        'raza': 'Labrador',
        'lugar_perdido': 'Parque Central',
        'fecha_perdida': '2024-11-01',
        'info_adicional': 'Llevaba un collar rojo',
        'descripcion': 'Perro activo y juguetón.',
        'otros_comentarios': 'Es muy amigable con las personas.',
        'foto_url': 'images/perro.jpg'
    },
    {
        'id': 2,
        'nombre': 'Taya',
        'animal': 'Gato',
        'raza': 'Siames',
        'lugar_perdido': 'Calle 42',
        'fecha_perdida': '2024-10-29',
        'info_adicional': 'Es muy tímido',
        'descripcion': 'Gato de tamaño medio con pelaje corto.',
        'otros_comentarios': 'No se lleva bien con otros gatos.',
        'foto_url': 'images/gato.webp'
    },
    {
        'id': 3,
        'nombre': 'Maco',
        'animal': 'Perro',
        'raza': 'Labrador',
        'descripcion': 'Encontramos este perro con collar por San Isidro.',
        'foto_url': 'images/perro2.webp'
    },
    {
        'id': 4,
        'nombre': 'Caco',
        'animal': 'Hamster',
        'raza': 'Chino',
        'descripcion': 'Encontramos este hamster perdido, comunicarse si conoce al dueño.',
        'foto_url': 'images/hamster.jpg'
    },
    {
        'id': 5,
        'nombre': 'Mirinda',
        'animal': 'Loro',
        'raza': 'Guacamayo',
        'descripcion': 'Loro perdido en la zona de Moron.',
        'foto_url': 'images/loro.jpg'
    },
    {
        'id': 6,
        'nombre': 'Jack',
        'animal': 'Gato',
        'raza': 'Siames',
        'descripcion': 'Gato siames encontrado, con un collar con el nombre Jack.',
        'foto_url': 'images/gato2.jpg'
    }
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
