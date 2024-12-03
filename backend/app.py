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
    nombre_filtro = request.args.get("filtro")

    if nombre_filtro:
        query = """
        SELECT * FROM mascotas 
        WHERE nombre LIKE :filtro 
        OR raza LIKE :filtro 
        OR color LIKE :filtro 
        OR estado LIKE :filtro
        OR animal LIKE :filtro
    """
        query_params = {"filtro": f"%{nombre_filtro}%"}
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
                "fecha": row[6],
                "descripcion": row[7],
                "estado": row[8],
                "imagen": row[9],
                "latitud": row[10],
                "longitud": row[11],
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
        "telefono",
        "email",
        "fecha",
        "descripcion",
        "estado",
        "imagen",
        "latitud",
        "longitud",
    )
    for key in keys:
        if key not in data:
            return jsonify({"error": f"Falta el dato {key}"}), 400

    try:

        query_1 = f"""INSERT INTO mascotas (nombre, animal,raza,color,edad,fecha,descripcion,estado,imagen,latitud,longitud) 
        VALUES ('{data["nombre"]}','{data["animal"]}','{data["raza"]}','{data["color"]}','{data["edad"]}','{data["fecha"]}',
        '{data["descripcion"]}','{data["estado"]}','{data["imagen"]}','{data["latitud"]}','{data["longitud"]}');"""

        conn.execute(text(query_1))
        mascota_id = conn.execute(text("SELECT LAST_INSERT_ID();")).scalar()

        query_2 = f""" INSERT INTO personas (mascotaID, telefono, email) 
        VALUES ({mascota_id},'{data["telefono"]}','{data["email"]}');"""
        
        conn.execute(text(query_2))
        conn.commit()

    except SQLAlchemyError as err:
        print("error", err.__cause__)

    return jsonify({"message": "se a agregado correctamente" + query_1 + query_2}), 201


@app.route("/mascotasPorID/<int:mascotaID>", methods=["GET"])
def mascotas_por_ID(mascotaID):
    conn = set_connection()
    query = """SELECT nombre,animal,raza,color,edad,fecha,descripcion,estado,imagen,latitud,longitud, personas.telefono, personas.email 
               FROM mascotas
               INNER JOIN personas ON mascotas.mascotaID = personas.mascotaID 
               WHERE mascotas.mascotaID = :mascotaID"""

    try:
        params = {"mascotaID": mascotaID}
        result = conn.execute(text(query), params).fetchall()
    except SQLAlchemyError as err:
        print("error", err.__cause__)

    if len(result) == 0:
        return jsonify({"error": "no se encontro la mascota"}), 404

    response = []
    for row in result:
        response.append(
            {
                "nombre": row[0],
                "animal": row[1],
                "raza": row[2],
                "color": row[3],
                "edad": row[4],
                "fecha": row[5],
                "descripcion": row[6],
                "estado": row[7],
                "imagen": row[8],
                "latitud": row[9],
                "longitud": row[10],
                "telefono": row[11],
                "email": row[12],
            }
        )

    return jsonify(response), 200


@app.route("/mascotaBorrar/<int:mascotaID>", methods=["DELETE"])
def mascotaBorrar(mascotaID):
    conn = set_connection()
    query = """SELECT nombre,animal,raza,color,edad,fecha,descripcion,estado,imagen,latitud,longitud, personas.telefono, personas.email 
               FROM mascotas
               INNER JOIN personas ON mascotas.mascotaID = personas.mascotaID 
               WHERE mascotas.mascotaID = :mascotaID"""
    query1 = """DELETE FROM personas WHERE mascotaID = :mascotaID"""
    query2 = """DELETE FROM mascotas WHERE mascotaID = :mascotaID"""
    try:
        params = {"mascotaID": mascotaID}
        result = conn.execute(text(query), params).fetchall()
        if len(result) == 0:
            return jsonify({"error": "No se encontro la mascota"}), 404
        conn.execute(text(query1), params)
        conn.execute(text(query2), params)
        conn.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    conn.close()

    return jsonify({"correcto": "se a eliminado correctamente"}), 200


@app.route("/filtro_mascota", methods=["GET"])
def mascotas_filtro():
    conn = set_connection()

    animal = request.args.get("animal", "")
    raza = request.args.get("raza", "")
    edad = request.args.get("edad", "")
    color = request.args.get("color", "")
    estado = request.args.get("estado", "")

    query = "SELECT * FROM mascotas WHERE 1=1"  # '1=1' es una condición siempre verdadera, útil para construir dinámicamente

    # Crear el diccionario para los parámetros de la consulta
    query_params = {}

    # Agregar filtros a la consulta solo si tienen un valor
    if animal:
        query += " AND animal = :animal"
        query_params["animal"] = animal

    if raza:
        query += " AND raza = :raza"
        query_params["raza"] = raza

    if edad:
        query += " AND edad = :edad"
        query_params["edad"] = edad

    if color:
        query += " AND color = :color"
        query_params["color"] = color
    
    if estado:
        query += " AND estado = :estado"
        query_params["estado"] = estado

    try:
        result = conn.execute(text(query), query_params)
    except SQLAlchemyError as e:
        print(f"Error ejecutando la consulta: {e}")
        return jsonify({"error": "Error en la consulta SQL"}), 500

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
                "fecha": row[6],
                "descripcion": row[7],
                "estado": row[8],
                "imagen": row[9],
                "latitud": row[10],
                "longitud": row[11],
            }
        )

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
