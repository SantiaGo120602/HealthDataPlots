from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plotting")
def plotting_page():
    return render_template("plotting.html")


if __name__ == "__main__":
    app.run()