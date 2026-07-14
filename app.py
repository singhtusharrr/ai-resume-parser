from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from utils.parser import extract_text_from_pdf
from utils.ai import analyze_resume

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a PDF"

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    resume_text = extract_text_from_pdf(filepath)

    ai_result = analyze_resume(resume_text)

    return render_template(
        "result.html",
        result=ai_result
    )