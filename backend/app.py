from flask import Flask
import csv
import pandas as pd


app = Flask('__name__')
insurance_data_csv = '../data/data_set_insurance.csv'

@app.route('/')
def hello_world():
    output = []
    with open(insurance_data_csv, newline='') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            print(', '.join(row))



