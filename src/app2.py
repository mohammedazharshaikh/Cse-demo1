from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    image_url = f'/static/images/{name}.jpg'
    # image_url = 'https://cse5332storage1.blob.core.windows.net/container1/sriya.jpg?sp=r&st=2024-06-06T03:52:26Z&se=2024-06-06T11:52:26Z&spr=https&sv=2022-11-02&sr=b&sig=DPrcACwjKPKeDB3saQe5vjI2LfEOPLTn4qj1o9NRoXw%3D'

    # Construct the image URL did we need to give container img link?
    return render_template('result.html', name=name, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
