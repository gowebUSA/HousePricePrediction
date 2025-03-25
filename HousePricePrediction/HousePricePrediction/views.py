from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

# def result(request):
#
#     data = pd.read_csv(r"C:\Users\goric\Downloads\USA_Housing.csv")
#     data = data.drop(['Address'], axis=1)
#     X = data.drop(['Price'], axis=1)
#     Y = data['Price']
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)
#     model = LinearRegression()
#     model.fit(X_train, Y_train)
#
#     var1 = float(request.GET['n1'])
#     var2 = float(request.GET['n2'])
#     var3 = float(request.GET['n3'])
#     var4 = float(request.GET['n4'])
#     var5 = float(request.GET['n5'])
#
#     # pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,-1))
#     # pred = round(pred[0])
#     input_data = pd.DataFrame([[var1, var2, var3, var4, var5]], columns=X.columns)
#     pred = model.predict(input_data)
#     # pred = round(pred[0])
#
#     price = "The predicted price is $"+str(pred)
#
#     return render(request, "predict.html", {"result2":price})

def result(request):
    data = pd.read_csv(r"C:\Users\goric\Downloads\USA_Housing.csv")
    data = data.drop(['Address'], axis=1)
    X = data.drop(['Price'], axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Get user input safely
    var1 = float(request.GET.get('n1', 0))
    var2 = float(request.GET.get('n2', 0))
    var3 = float(request.GET.get('n3', 0))
    var4 = float(request.GET.get('n4', 0))
    var5 = float(request.GET.get('n5', 0))

    # Convert input to DataFrame with feature names
    input_data = pd.DataFrame([[var1, var2, var3, var4, var5]], columns=X.columns)

    pred = model.predict(input_data)
    pred = round(pred[0])

    price = f"The predicted price is ${pred:,}"

    return render(request, "predict.html", {"result2": price})

