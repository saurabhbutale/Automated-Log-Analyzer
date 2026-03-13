from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def analyze_log(file_path):
    errors = []
    warnings = []
    info = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)
            elif "INFO" in line:
                info.append(line)

    return errors, warnings, info


@app.route("/", methods=["GET", "POST"])
def index():
    errors = []
    warnings = []
    info = []

    if request.method == "POST":
        file = request.files["logfile"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            errors, warnings, info = analyze_log(filepath)

    return render_template(
        "index.html",
        errors=errors,
        warnings=warnings,
        info=info
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)