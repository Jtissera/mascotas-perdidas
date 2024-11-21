from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

def set_connection():
    engine = create_engine("mysql+mysqlconnector://vouteda:password@localhost:3306/MascotasPerdidasDB")
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
        print("Database error:", err.__cause__)
        return jsonify({"error": "Error al consultar las mascotas"}), 500

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

    conn.close()
    return jsonify(response), 200

@app.route("/mascota/<int:mascota_id>", methods=["GET"])
def get_mascota(mascota_id):
    conn = set_connection()

    query = "SELECT * FROM mascotas WHERE mascotaID = :mascota_id"
    query_params = {'mascota_id': mascota_id}

    try:
        result = conn.execute(text(query), query_params).fetchone()
    except SQLAlchemyError as err:
        print("Database error:", err.__cause__)
        return jsonify({"error": "Error al consultar la mascota"}), 500

    if not result:
        return jsonify({"error": "Mascota no encontrada"}), 404

    response = {
        "mascotaID": result[0],
        "nombre": result[1],
        "animal": result[2],
        "raza": result[3],
        "color": result[4],
        "edad": result[5],
        "zona": result[6],
        "fecha": result[7],
        "descripcion": result[8],
        "estado": result[9],
        "imagen": result[10]
    }

    conn.close()
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
