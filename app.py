from flask import *
from werkzeug.utils import secure_filename
import os
from stylise import *
from globals import *

# Instantiating the flask appliction and configuriating the templates folder
app = Flask(__name__, template_folder="C:\\Users\\samue\\Desktop\\creativecomputinga1\\templates")
app.config['UPLOAD_FOLDER'] = "C:\\Users\\samue\\Desktop\\creativecomputinga1\\UPLOAD_FOLDER"
app.config['OUT_FOLDER'] = "C:\\Users\\samue\\Desktop\\creativecomputinga1\\OUT_FOLDER"
# Secret key is required for error handling and Flask Flash capabilities.
app.secret_key = '1238972198372987fddsf'


# Function to check whether the uploaded file contains an allowed extension by splitting the last characters.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newpath = uploadpath + "\\" + filename
            dropdown_value = request.form.get('dropdown')
            stylise(newpath, filename, dropdown_value)
            return render_template('uploaded_file.html', filename=filename)

        flash('Error: Unsupported file type')
        return redirect(request.url)

    return render_template('upload_file.html')

# Function to redirect to the uploads page.
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['OUT_FOLDER'], filename)


app.run(host='0.0.0.0', port=3000)
