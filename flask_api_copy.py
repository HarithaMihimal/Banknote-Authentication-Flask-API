from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"
@app.route('/predict')
def predict_note_authentication():

    """ Lets Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
      200:
        description: The prediction value
      400:
        description: Bad Request
      500:
        description: Internal Server Error
    """


    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return f"The prediction value is {prediction}"


@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    """ Lets Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    
    responses:
      200:
        description: The prediction value
      400:
        description: Bad Request
      500:
        description: Internal Server Error
    """

    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    return f"The prediction value for the csv is {prediction.tolist()}"

if __name__ == '__main__':
    app.run(debug=True)