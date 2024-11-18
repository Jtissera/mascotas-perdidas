from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://vouteda:password@localhost:3306/MascotasPerdidasDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking (optional)

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Flag to ensure create_all runs only once
created_tables = False

# Define the Mascota model
class Mascota(db.Model):
    __tablename__ = 'mascotas'

    mascotaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    animal = db.Column(db.String(255), nullable=False)
    raza = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    edad = db.Column(db.String(255), nullable=True)
    zona = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=True)
    descripcion = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.String(255), nullable=True)
    imagen = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Mascota {self.nombre}>"

# Create tables only once using a flag
@app.before_request
def create_tables():
    global created_tables
    if not created_tables:
        db.create_all()  # This creates the tables
        created_tables = True  # Set flag to True after tables are created

# Endpoint to fetch all mascotas or search by filtro
@app.route("/mascotas", methods=["GET"])
def mascotas():
    nombre_filtro = request.args.get('filtro')

    if nombre_filtro:
        # Querying the database with filter
        mascotas = Mascota.query.filter(
            Mascota.nombre.like(f"%{nombre_filtro}%") |
            Mascota.raza.like(f"%{nombre_filtro}%") |
            Mascota.color.like(f"%{nombre_filtro}%") |
            Mascota.zona.like(f"%{nombre_filtro}%") |
            Mascota.estado.like(f"%{nombre_filtro}%") |
            Mascota.animal.like(f"%{nombre_filtro}%")
        ).all()
    else:
        mascotas = Mascota.query.all()

    response = [
        {
            "mascotaID": mascota.mascotaID,
            "nombre": mascota.nombre,
            "animal": mascota.animal,
            "raza": mascota.raza,
            "color": mascota.color,
            "edad": mascota.edad,
            "zona": mascota.zona,
            "fecha": mascota.fecha,
            "descripcion": mascota.descripcion,
            "estado": mascota.estado,
            "imagen": mascota.imagen
        }
        for mascota in mascotas
    ]

    return jsonify(response), 200

@app.route("/mascota/<int:mascota_id>", methods=["GET"])
def get_mascota(mascota_id):
    # Fetch the Mascota by ID or return a 404 error if not found
    mascota = Mascota.query.get_or_404(mascota_id)

    # Prepare the response data
    response = {
        "mascotaID": mascota.mascotaID,
        "nombre": mascota.nombre,
        "animal": mascota.animal,
        "raza": mascota.raza,
        "color": mascota.color,
        "edad": mascota.edad,
        "zona": mascota.zona,
        "fecha": mascota.fecha,
        "descripcion": mascota.descripcion,
        "estado": mascota.estado,
        "imagen": mascota.imagen
    }

    return jsonify(response)


# Endpoint to create a new mascota
@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    data = request.get_json()

    # Check if all required fields are in the received data
    required_keys = [
        "nombre", "animal", "raza", "color", "edad", "zona",
        "telefono", "email", "fecha", "descripcion", "imagen"
    ]
    
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"Falta el dato {key}"}), 400

    # Create a new Mascota record
    nueva_mascota = Mascota(
        nombre=data["nombre"],
        animal=data["animal"],
        raza=data["raza"],
        color=data["color"],
        edad=data["edad"],
        zona=data["zona"],
        fecha=data["fecha"],  # Assuming it's already in the correct format
        descripcion=data["descripcion"],
        imagen=data["imagen"],
        estado=data.get("estado", "perdida")  # Default to "perdida" if no state is provided
    )

    # Add and commit the new record for mascotas
    try:
        db.session.add(nueva_mascota)
        db.session.commit()

        # Insert persona info (assumes the `persona` table exists)
        nueva_persona = Persona(
            telefono=data["telefono"],
            email=data["email"]
        )
        db.session.add(nueva_persona)
        db.session.commit()

    except SQLAlchemyError as err:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": f"Database error: {str(err)}"}), 500

    return jsonify({"message": "Mascota creada correctamente!"}), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
