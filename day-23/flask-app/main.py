from flask import Flask, render_template, request, flash
import os
from werkzeug.utils import secure_filename
import cv2

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


def processImage(filename, operation):
    print(f"The filename is {filename} and the operation is {operation}")
    img = cv2.imread(f"uploads/{filename}")
    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFileName = f"static/{filename}"
            cv2.imwrite(newFileName, imgProcessed)
            return filename
        case "cwebp":
            newFileName = f"static/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFileName, img)
            return newFileName
        case "cjpg":
            newFileName = f"static/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFileName, img)
            return newFileName
        case "cpng":
            newFileName = f"static/{filename.split('.')[0]}.png"
            cv2.imwrite(newFileName, img)
            return newFileName


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error no Selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = processImage(filename, operation)
            flash("Your Image has been processed and it is available "
                  f"<a herf='/{new}' target='_blank'>here</a>")
            return render_template("index.html")
    return render_template("index.html")


app.run(debug=True)
