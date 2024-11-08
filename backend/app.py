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
                "raza": row[1],
                "color": row[2],
                "edad": row[3],
                "zona": row[4],
                "fecha": row[5],
                "descripcion": row[6],
                "estado": row[7],
            }
        )

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
