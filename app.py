from flask import Flask, render_template, request, redirect, url_for
import os
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/sobre-mim", methods=["GET"])
def sobreMim():
    return render_template("sobre-mim.html")

@app.route("/formacao", methods=["GET"])
def formacao():
    return render_template("formacao.html")

@app.route("/projetos", methods=["GET"])
def projetos():
    return render_template("projetos.html")

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()

app.run(debug=True)