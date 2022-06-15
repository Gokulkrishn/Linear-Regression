from crypt import methods
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [int(each) for each in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = np.round(prediction[0],2)[0]
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))   

if __name__ == "__main__":
    app.run(debug=True)    