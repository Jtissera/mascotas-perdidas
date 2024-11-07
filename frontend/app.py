from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index-1")
def index_1():
    return render_template("index-1.html")


@app.route("/index-2")
def index_2():
    return render_template("index-2.html")


@app.route("/index-3")
def index_3():
    return render_template("index-3.html")


@app.route("/index-4")
def index_4():
    return render_template("index-4.html")


@app.route("/index-5")
def index_5():
    return render_template("index-5.html")


@app.route("/homeV1")
def homeV1():
    return render_template("homeV1.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
