from flask import Flask, render_template, request
import requests


API_URL = 'http://localhost:8080/'
app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


import requests  # Make sure you're using the requests module

@app.route("/perdi_mi_mascota")
def perdi_mi_mascota():
    # Retrieve the search filter parameter from the URL
    mascotas_info = request.args.get('fsearch')  # `request` here is Flask's request object, for URL params
    params = {'filtro': mascotas_info}

    try:
        # Make an external API request using the 'requests' library
        response = requests.get(API_URL + 'mascotas', params=params)
        response.raise_for_status()  # This will raise an exception for 4xx/5xx HTTP status codes
        mascotas = response.json()  # Parse the JSON response from the API
    except requests.exceptions.RequestException as e:  # Handle errors from the requests library
        print(f"Error fetching data: {e}")  # Log error to the console for debugging
        mascotas = []  # In case of an error, return an empty list

    # Print the response to the server's console for debugging
    print(mascotas)

    # Render the template and pass the mascotas data to the template
    return render_template("perdi_mi_mascota.html", mascotas=mascotas)


@app.route("/encontre_una_mascota", methods=["GET","POST"])
def encontre_una_mascota():
    if request.method == "POST":
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
            "imagen": request.form.get("fimage")
        }
        try:
            response = requests.post(API_URL + 'crear_mascota', json=formulario_data)
            response.raise_for_status() 

        except requests.exceptions.RequestException as e:
            print(f"Error al enviar los datos a la API: {e}")
            return jsonify({"error": "Hubo un problema al enviar los datos."}), 500
        
        return render_template("homeV1.html")
    
    return render_template("encontre_una_mascota.html")

@app.route('/mascota/<int:mascota_id>')
def mostrar_mascota(mascota_id):
    try:
        # Make a GET request to the backend to fetch the pet data by ID
        response = requests.get(f'http://localhost:8080/mascota/{mascota_id}')
        response.raise_for_status()  # Raise an exception if the request was not successful
        mascota = response.json()  # Parse the JSON response

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return f"Error: {e}", 500  # Handle the error appropriately

    # Pass the fetched mascota data to the template
    return render_template('mascota_perdida.html', mascota=mascota)


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
