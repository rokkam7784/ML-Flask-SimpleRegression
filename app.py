import numpy as np
from flask import Flask, request, jsonify, render_template,make_response
import pickle

# creating a flask app
app = Flask(__name__,template_folder="views/templates",static_folder="views/static")

# loading the pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])

def welcome():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return "Bad Request"

@app.route('/predict/<yrsOfExperience>')
def predict(yrsOfExperience):
    if request.method == 'GET':        
        yrsOfExperience = float(yrsOfExperience)
        prediction = model.predict([[yrsOfExperience]])
        result = {"YearsOfExperience": yrsOfExperience,
                "Salary": int(prediction[0])}
        res = make_response(jsonify(result))
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Headers"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "*"
        return res
    else:
        return"Bad Request"


if __name__ == "__main__":
    app.run()