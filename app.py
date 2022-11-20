from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/sobre-mim", methods=["GET", "POST"])
def sobreMim():
    return render_template("sobre-mim.html")

@app.route("/formacao", methods=["GET", "POST"])
def formacao():
    return render_template("formacao.html")

@app.route("/projetos", methods=["GET", "POST"])
def projetos():
    return render_template("projetos.html")

app.run(debug=True)