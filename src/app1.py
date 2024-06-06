from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Ensure there is a folder to save the uploaded files
os.makedirs('uploads', exist_ok=True)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        # Read the CSV
        df = pd.read_csv(filepath)
        return df.to_html()
    else:
        return 'Invalid file type'

if __name__ == '__main__':
    app.run(debug=True)
