from flask import Flask, request
import PredictionModule as pd
from flask_cors import cross_origin
from flask import jsonify
from PIL import Image
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/predict', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def predict():
    result='correct'
    files = request.get_data('file').decode('UTF-8')
    print(files)
    img = Image.open(files)
    result = pd.predict(img)
    print(result)
    return jsonify(result=result, path=files)

if __name__ == '__main__':
   app.run(debug = True)