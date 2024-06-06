# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads/'  # Define the upload folder path
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# print(app.static_folder)  # This will show you the path being used for static files

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         name = request.form['name']
#         file = request.files['file']
#         if file and name:
#             filename = name + '_' + file.filename  # Customize the filename to include the name input
#             save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(save_path)  # Save the file
#             return redirect(url_for('uploaded_file', filename=filename))   
#     return render_template('upload1.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return render_template('display.html', filename=filename)

# @app.route('/test-files')
# def test_files():
#     from os import listdir
#     from os.path import isfile, join
#     files_list = [f for f in listdir(app.config['UPLOAD_FOLDER']) if isfile(join(app.config['UPLOAD_FOLDER'], f))]
#     return str(files_list)  # Display list of files in browser



# if __name__ == '__main__':
#     app.run(debug=True)

# ---
# --
# from flask import Flask, request, render_template, redirect, url_for
# import pandas as pd
# import os

# app = Flask(__name__)
# DATA_FILE = 'src/people.csv'
# UPLOAD_FOLDER = '/static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         name = request.form['name'].strip().lower()
#         file = request.files['file']

#         if file:
#             df = pd.read_csv(DATA_FILE)
#             # Check if the name exists in the DataFrame
#             if name in df['Name'].values:
#                 # Update the 'Picture' column with the new file name
#                 df.loc[df['Name'] == name, 'Picture'] = file.filename
#                 # Save the DataFrame back to CSV
#                 df.to_csv(DATA_FILE, index=False)
#                 # Save the file
#                 file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#                 file.save(file_path)
#                 return redirect(url_for('index'))
#             else:
#                 return render_template('upload1.html', message='Name not found in the record')
#         else:
#             return render_template('upload1.html', message='No file uploaded')

#     return render_template('upload1.html', message=None)

# if __name__ == "__main__":
#     app.run(debug=True)
# ---


import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            print("filename:"+ filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # file.save(save_path)
            # print("Save path:", save_path)
            # print("Full path:", os.path.abspath(save_path))
            print("Current working directory:", os.getcwd())


            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload1.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print(url_for('static', filename='uploads/' + filename))  # Debug print
    return render_template('display.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

#---
# testing
# import os
# from flask import Flask

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# # Ensure the upload directory exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# @app.route('/test-write')
# def test_write():
#     test_path = os.path.join(app.config['UPLOAD_FOLDER'], 'testfile.txt')
#     try:
#         with open(test_path, 'w') as f:
#             f.write('Hello World')
#         return "File written successfully!"
#     except Exception as e:
#         return f"Error writing test file: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)
