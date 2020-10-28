from flask import Flask, render_template, redirect, jsonify
from bson import ObjectId
import json
import pandas as pd

# Create an instance of Flask
app = Flask(__name__)

bikes=pd.read_csv('https://ncdanzerzones-ds.s3.us-east-2.amazonaws.com/bikes.csv', delimiter=",", dtype=str)
del bikes['Unnamed: 0']

pedes=pd.read_csv('https://ncdanzerzones-ds.s3.us-east-2.amazonaws.com/pedes.csv', delimiter=",", dtype=str)
del pedes['Unnamed: 0']

@app.route("/")
def welcome():
    """List all available api routes."""
    return render_template("welcome.html")

@app.route("/pedes_chart")
def pedes_chart():

    return render_template("index_peds.html")

@app.route("/bikes_chart")
def bikes_chart():

    return render_template("index_bikes.html")

@app.route("/read_bikes")
def read_bikes():
    output = {}

    for i in range(len(bikes)):
        county=bikes['County'].iloc[i]
        year=bikes['CrashYear'].iloc[i]
        month=bikes['CrashMonth'].iloc[i]
        day_of_week=bikes['Day of Week'].iloc[i]
        crash_hour=bikes['CrashHour'].iloc[i]
        speed_limit=bikes['SpeedLimit_upper_value'].iloc[i]
        age=bikes['Age'].iloc[i]
        output.update( {county : (year, month, day_of_week, crash_hour, speed_limit, age)} )

    return jsonify(output)

@app.route("/read_pedestrians")
def read_pedestrians():

    output = {}

    for i in range(len(pedes)):
        county=pedes['County'].iloc[i]
        year=pedes['CrashYear'].iloc[i]
        month=pedes['CrashMonth'].iloc[i]
        day_of_week=pedes['Day of Week'].iloc[i]
        crash_hour=pedes['CrashHour'].iloc[i]
        speed_limit=pedes['SpeedLimit_upper_value'].iloc[i]
        age=pedes['Age'].iloc[i]
        output.update( {county : (year, month, day_of_week, crash_hour, speed_limit, age)} )
    
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)

