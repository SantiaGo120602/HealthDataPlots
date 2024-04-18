from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_ngrok import run_with_ngrok
from datetime import datetime


app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()