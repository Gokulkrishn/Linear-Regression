from cmath import log
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle,sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    try:
        raise Exception("We are testing exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info("We are testing logging module1")
        logging.info(housing.error_message)
        logging.info("We are testing logging module2")
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on html GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = np.round(prediction[0], 2)[0]

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)