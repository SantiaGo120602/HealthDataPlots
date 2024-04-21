from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wfdb_processing.paths import get_bases_and_path_dict

WFDB_BASES_NAMES, WFDB_TO_RECORD = get_bases_and_path_dict()
CURRENT_BASE = WFDB_BASES_NAMES[1]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plotting")
def plotting_page():
    return render_template("plotting.html")

@app.route("/wfdb_databases")
def databases_page():
    global CURRENT_BASE
    return render_template("wfdb_databases.html", wfdb_sources = WFDB_BASES_NAMES)

@app.route("/process_data", methods=["POST"])
def process_data():
    if request.method == "POST":
        source = request.form.get("source")  # Get the value of 'source' from the POST request
        # Process the data as needed
        # Return a response if needed
        return "/plotting"

if __name__ == "__main__":
    app.run()