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



if __name__ == "__main__":
    app.run(debug=True)