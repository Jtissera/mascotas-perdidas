from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)


def set_connection():
    engine = create_engine(
        "mysql+mysqlconnector://root:root@localhost:3306/MascotasPerdidasDB"
    )

    connection = engine.connect()
    return connection


@app.route("/mascotas", methods=["GET"])
def mascotas():
    conn = set_connection()
    nombre_filtro = request.args.get('filtro')

    if nombre_filtro:
        query = """
        SELECT * FROM mascotas 
        WHERE nombre LIKE :filtro 
        OR raza LIKE :filtro 
        OR color LIKE :filtro 
        OR zona LIKE :filtro 
        OR estado LIKE :filtro
        OR animal LIKE :filtro
    """
        query_params = {'filtro': f'%{nombre_filtro}%'}
    else:
        query = "SELECT * FROM mascotas"
        query_params = {}

    try:
        result = conn.execute(text(query), query_params)
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

    print("Datos recibidos:", data)

    keys = ("nombre","animal","raza","color","edad","zona",
	"telefono","email","fecha","descripcion","imagen"
    )
    for key in keys:
        if key not in data:
            return jsonify({"error": f"Falta el dato {key}"}), 400

    query_1 = f"""INSERT INTO mascotas (nombre, animal,raza,color,edad,zona,fecha,descripcion,imagen) 
    VALUES ('{data["nombre"]}','{data["animal"]}','{data["raza"]}','{data["color"]}','{data["edad"]}','{data["zona"]}','{data["fecha"]}','{data["descripcion"]}','{data["imagen"]}');"""
    
    query_2 = f"""INSERT INTO personas (telefono, email) 
    VALUES ('{data["telefono"]}','{data["email"]}');"""

    try:
        conn.execute(text(query_1))
        conn.execute(text(query_2))
        conn.commit()

    except SQLAlchemyError as err:
        print("error", err.__cause__)

    return jsonify({"message": "se a agregado correctamente" + query_1 + query_2}), 201

@app.route("/mascotasPorID/<int:mascotaID>", methods=["GET"])
def mascotas_por_ID(mascotaID):
    conn = set_connection()
    query = """SELECT nombre,animal,raza,color,edad,zona,fecha,descripcion,estado,imagen, personas.telefono, personas.email 
               FROM mascotas
               INNER JOIN personas ON mascotas.mascotaID = personas.mascotaID WHERE mascotas.mascotaID = :mascotaID"""

    try:
        params = {'mascotaID':mascotaID}
        result = conn.execute(text(query),params).fetchall()
    except SQLAlchemyError as err:
        print("error", err.__cause__)

    conn.close()

    if len(result) == 0:
        return jsonify({'error': 'no se encontro la mascota'}), 404

    response = []
    for row in result:
        response.append(
            {
            	"nombre": row[0],
            	"animal": row[1],
            	"raza": row[2],
            	"color": row[3],
            	"edad": row[4],
            	"zona": row[5],
            	"fecha": row[6],
            	"descripcion": row[7],
            	"estado": row[8],
                "imagen": row[9],
                "telefono": row[10],
                "email": row[11],
            }
        )

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
