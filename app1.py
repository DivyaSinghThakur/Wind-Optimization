import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\divya\\Downloads\\wind_optimization_final\\wind_optimization\\pickel1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('flask.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    prediction = model.predict(features_value)
 
    output = (prediction[0])
    output=round(output,2)
    print(output)

        

    return render_template('flask.html', prediction_text=f'Active Power will be {output:.2f} kwatt')

if __name__ == "__main__":
    app.run(debug=True)