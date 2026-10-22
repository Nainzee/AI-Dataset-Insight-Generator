from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from backend.pipeline import run_pipeline

app = Flask(__name__, template_folder="../templates", static_folder="../static")

UPLOAD_FOLDER = "data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded. Please select a CSV file."}), 400

    file = request.files["file"]
    if not file or file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    try:
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        insights = run_pipeline(filepath)
        return jsonify(insights)
    except Exception as e:
        app.logger.exception("Error processing dataset upload")
        return jsonify({"error": f"Failed to analyze dataset: {str(e)}"}), 500

@app.route('/charts/<path:filename>')
def serve_chart(filename):
    return send_from_directory('../visualization/outputs', filename)


if __name__ == "__main__":
    app.run(debug=True)