import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# creating a flask app
app = Flask(__name__)

# loading the pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return " "

@app.route('/YearsOfExperience/<float:yrsOfExperience>')
def predict(yrsOfExperience):
    prediction = model.predict([[yrsOfExperience]])
    result = {"YearsOfExperience": yrsOfExperience,
              "Salary": int(prediction[0])}
    return result


if __name__ == "__main__":
    app.run(debug=True)