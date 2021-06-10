import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# creating a flask app
app = Flask(__name__)

# loading the pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def hello_world():
    if request.method == 'GET':
        return " "
    else:
        return "Bad Request"


# TODO: Make a website for this function
@app.route('/YearsOfExperience/<yrsOfExperience>',methods=['GET'])
def predict(yrsOfExperience):
    if request.method == 'GET':
        try:
            yrsOfExperience = float(yrsOfExperience)
            prediction = model.predict([[yrsOfExperience]])
            result = {"YearsOfExperience": yrsOfExperience,
                    "Salary": int(prediction[0])}
            return result
        except ValueError:
            return "Enter a numerical value as years of experience"
    else:
        return"Bad Request"


if __name__ == "__main__":
    app.run(debug=True)