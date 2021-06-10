# Simple Linear Regression

# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# importing Dataset
dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# splitting the dataset into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Training the model on the Training set
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting the test set results
y_pred = regressor.predict(x_test)


def predict(yrsOfExperience):
    result = regressor.predict([[yrsOfExperience]])
    print(result)


# Saving model to disk
pickle.dump(regressor, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[4.4]]))
