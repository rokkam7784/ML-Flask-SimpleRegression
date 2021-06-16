import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# creating a flask app
app = Flask(__name__,template_folder="views/templates",static_folder="views/static",)

# loading the pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def welcome():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return "Bad Request"

@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            yrsOfExperience = float(request.form['yrsOfExperience'])
            prediction = model.predict([[yrsOfExperience]])
            result = {"YearsOfExperience": yrsOfExperience,
                    "Salary": int(prediction[0])}
            return render_template("index.html")
    else:
        return"Bad Request"


if __name__ == "__main__":
    app.run(debug=True)