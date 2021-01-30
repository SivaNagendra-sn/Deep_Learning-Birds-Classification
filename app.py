from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from utility.utils import decodeImage
from predict import birds

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "Bird_img.jpg"
        self.classifier = birds(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.bird_classifier()
    return jsonify(result)


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()

    # app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=8000, debug=True)
