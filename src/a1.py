# DefaultEndpointsProtocol=https;AccountName=cse5332storage1;AccountKey=nsXNXTgM/yVWP0KzOcUbe6u7Ktth+f4BqTWSD3S4Mpmh/gZQMyDi7pJ3riXsaoCmr42QTl0O2nfu+AStpCi11w==;EndpointSuffix=core.windows.net

# app.py
# from flask import Flask, request, render_template, jsonify
# import os
# import csv
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# app = Flask(__name__)

# Azure Blob Storage configuration
# AZURE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=cse5332storage1;AccountKey=nsXNXTgM/yVWP0KzOcUbe6u7Ktth+f4BqTWSD3S4Mpmh/gZQMyDi7pJ3riXsaoCmr42QTl0O2nfu+AStpCi11w==;EndpointSuffix=core.windows.net'
# CONTAINER_NAME = 'container1'
# blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
# container_client = blob_service_client.get_container_client(CONTAINER_NAME)

from flask import Flask, render_template, request, jsonify
import os
import csv
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name__)

# Azure Blob Storage configuration

AZURE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=cse5332storage1;AccountKey=nsXNXTgM/yVWP0KzOcUbe6u7Ktth+f4BqTWSD3S4Mpmh/gZQMyDi7pJ3riXsaoCmr42QTl0O2nfu+AStpCi11w==;EndpointSuffix=core.windows.net'
CONTAINER_NAME = 'container1'
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# In-memory storage for CSV data
people_data = {}

@app.route('/')
def home():
    return "Welcome to the Azure CSV CRUD app!"

@app.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file provided", 400

        content = file.read().decode('utf-8').splitlines()
        reader = csv.reader(content)
        next(reader)  # Skip header row
        for row in reader:
            name, salary, room, telnum, picture, keywords = row
            people_data[name] = {
                'salary': salary,
                'room': room,
                'telnum': telnum,
                'picture': picture,
                'keywords': keywords
            }
        return "CSV data uploaded successfully", 200
    return render_template('upload_csv.html')

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        data = request.json
        people_data[data['name']] = data
        return "Person added successfully", 201
    return render_template('add_person.html')

@app.route('/get_person', methods=['GET', 'POST'])
def get_person():
    if request.method == 'POST':
        name = request.form['name']
        person = people_data.get(name)
        if not person:
            return "Person not found", 404
        return jsonify(person), 200
    return render_template('get_person.html')

@app.route('/update_person', methods=['GET', 'POST'])
def update_person():
    if request.method == 'POST':
        data = request.json
        name = data['name']
        if name not in people_data:
            return "Person not found", 404
        people_data[name].update(data)
        return "Person updated successfully", 200
    return render_template('update_person.html')

@app.route('/delete_person', methods=['GET', 'POST'])
def delete_person():
    if request.method == 'POST':
        name = request.form['name']
        if name not in people_data:
            return "Person not found", 404
        del people_data[name]
        return "Person deleted successfully", 200
    return render_template('delete_person.html')

@app.route('/upload_picture', methods=['GET', 'POST'])
def upload_picture():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file provided", 400

        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(file)
        return "Picture uploaded successfully", 200
    return render_template('upload_picture.html')

@app.route('/get_picture', methods=['GET', 'POST'])
def get_picture():
    if request.method == 'POST':
        filename = request.form['filename']
        blob_client = container_client.get_blob_client(filename)
        if not blob_client.exists():
            return "Picture not found", 404

        blob_data = blob_client.download_blob().readall()
        return blob_data, 200, {'Content-Type': 'image/jpeg'}
    return render_template('get_picture.html')

if __name__ == '__main__':
    app.run(debug=True)
