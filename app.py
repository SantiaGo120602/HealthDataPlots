from flask import Flask, render_template, request, send_file
from wfdb_processing.paths import get_bases_and_path_dict
from wfdb_processing.plotting import generate_plot_and_comments

WFDB_BASES_NAMES, WFDB_TO_RECORD = get_bases_and_path_dict()
CURRENT_BASE = WFDB_BASES_NAMES[1]
CURRENT_PATIENT = WFDB_TO_RECORD[CURRENT_BASE][0]
PLOT_CONFIGURATION = {'scrollZoom': True, 'displaylogo': False}
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plotting")
def plotting_page():
    records = WFDB_TO_RECORD[CURRENT_BASE]
    records.sort()
    plot, comments = generate_plot_and_comments(CURRENT_PATIENT)
    plot_s = plot.to_html(full_html=False, config=PLOT_CONFIGURATION)

    if CURRENT_BASE == "bidmc-ppg-and-respiration-dataset-1.0.0":
        column_names = ("edad", "sexo", "Ubicación", "Fuente")
        column_values = tuple(com for com in comments.split(" ") if com[0] != "<")[:4]
    else:
        column_names = ["Tipo de prueba"]
        column_values = [comments]
    return render_template("plotting.html", plot_s = plot_s, records = records, column_values = column_values, column_names = column_names, patient = CURRENT_PATIENT)

@app.route("/wfdb_databases")
def databases_page():
    return render_template("wfdb_databases.html", wfdb_sources = WFDB_BASES_NAMES)

@app.route("/process_data", methods=["POST"])
def process_data():
    if request.method == "POST":
        source = request.form.get("source")
        global CURRENT_BASE, CURRENT_PATIENT
        CURRENT_BASE = source
        CURRENT_PATIENT = WFDB_TO_RECORD[CURRENT_BASE][0]
        return "/plotting"
    
@app.route("/update_record", methods=["POST"])
def update_record():
    if request.method == "POST":
        source = request.form.get("source")
        global CURRENT_PATIENT
        CURRENT_PATIENT = source
        return "/plotting"
    
@app.route("/download-report", methods=["GET"])
def download_report():
    file_path = CURRENT_PATIENT + ".hea"
    print(file_path)
    return send_file(file_path, as_attachment=True)

@app.route("/help")
def help_page():
    return render_template("help.html")

if __name__ == "__main__":
    app.run()