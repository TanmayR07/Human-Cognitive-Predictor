import os
import pickle

import numpy as np
from flask import Flask, jsonify, render_template, request

#app name
app = Flask(__name__)

#load the saved model
def load_model():
    return pickle.load(open('model.pkl', 'rb'))


#home page
@app.route('/')
def home():
    return render_template('index2.html')

#predict the result and return  it
@app.route('/predict_Human_Behaviour',methods=['POST'])
def predict():
    labels = ['recalled','imagined','retold']

    features = [int(x) for x in request.form.values()]

    values = [np.array(features)]

    model = load_model()
    predictions = model.predict(values)


    #result = labels[predictions[0]]
    return render_template('index2.html',output ='The dream is {}'.format(predictions[0]))

if __name__ == '__main__':
    #For Heroku
    #port = int(os.environ.get('PORT',5000))
    #app.run(port = port, debug= True,use_reloader = False)
    app.run(debug =True)
