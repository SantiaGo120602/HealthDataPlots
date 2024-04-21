from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

current_penis = "hola"

app = Flask(__name__)

@app.route("/")
def index():
    print(current_penis)
    return render_template("index.html")

@app.route("/plotting")
def plotting_page():
    global current_penis
    current_penis = "chao"
    print(current_penis)
    return render_template("plotting.html")


if __name__ == "__main__":
    app.run()