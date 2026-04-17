import pickle
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Use default '0' to avoid NoneType crash if any field is missing
        temperature = float(request.form.get('Temperature', 0))
        rh         = float(request.form.get('RH', 0))
        ws         = float(request.form.get('Ws', 0))
        rain       = float(request.form.get('Rain', 0))
        ffmc       = float(request.form.get('FFMC', 0))
        dmc        = float(request.form.get('DMC', 0))
        isi        = float(request.form.get('ISI', 0))
        classes    = float(request.form.get('CLASSES', 0))  # ← key fix
        region     = float(request.form.get('REGION', 0))

        new_data_scaled = standard_scaler.transform(
            [[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]]
        )
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', results=result[0])
    else:
        return render_template('home.html')  # safe GET fallback
if __name__ == '__main__':
    app.run(debug=True)
    print(standard_scaler.n_features_in_)