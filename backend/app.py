from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)


def set_connection():
    engine = create_engine(
        "mysql+mysqlconnector://root:franco@localhost:3306/MascotasPerdidasDB"
    )

    connection = engine.connect()
    return connection


@app.route("/mascotas", methods=["GET"])
def mascotas():
    conn = set_connection()
    query = "SELECT * FROM mascotas"
    try:
        result = conn.execute(text(query))
    except SQLAlchemyError as err:
        print("error", err.__cause__)

    response = []
    for row in result:
        response.append(
            {
                "mascotaID": row[0],
            	"nombre": row[1],
            	"animal": row[2],
            	"raza": row[3],
            	"color": row[4],
            	"edad": row[5],
            	"zona": row[6],
            	"fecha": row[7],
            	"descripcion": row[8],
            	"estado": row[9],
                "imagen": row[10]
            }
        )

    return jsonify(response), 200


@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    conn = set_connection()
    data = request.get_json()

    keys = (
	"nombre",
	"animal",
        "raza",
        "color",
        "edad",
        "zona",
	"telefono",
	"email",
        "fecha",
        "descripcion",
        "estado"
    )
    for key in keys:
        if key not in data:
            return jsonify({"error": f"Falta el dato {key}"}), 400

    query_1 = f"""INSERT INTO mascotas (nombre, animal,raza,color,edad,zona,fecha,descripcion,estado) 
    VALUES ('{data["nombre"]}','{data["animal"]}','{data["raza"]}','{data["color"]}','{data["edad"]}','{data["zona"]}','{data["fecha"]}','{data["descripcion"]}','{data["estado"]}');"""
    
    query_2 = f"""INSERT INTO personas (telefono, email) 
    VALUES ('{data["telefono"]}','{data["email"]}');"""

    try:
        conn.execute(text(query_1))
	conn.execute(text(query_2))
        conn.commit()

    except SQLAlchemyError as err:
        print("error", err.__cause__)

    return jsonify({"message": "se a agregado correctamente" + query_1 + query_2}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
