from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the files you dumped from Jupyter
model = joblib.load('Random_Forest_model.joblib')
encoder = joblib.load('encoder.joblib')
scaler = joblib.load('scaler.joblib')

# These must match your X.columns order exactly
NUM_COLS = ['hour', 'day', 'month', 'distance', 'surge_multiplier', 'temperature', 'humidity', 'pressure', 'is_rain']
CAT_COLS = ['source', 'destination', 'cab_type', 'name']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])

        # 1. OneHotEncode Categories
        cat_encoded = encoder.transform(input_df[CAT_COLS])
        cat_encoded_df = pd.DataFrame(cat_encoded, columns=encoder.get_feature_names_out())
        
        # 2. Combine with Numerical
        num_df = input_df[NUM_COLS].reset_index(drop=True)
        final_df = pd.concat([cat_encoded_df, num_df], axis=1)
        
        # 3. Scale Features
        final_scaled = scaler.transform(final_df)

        # 4. Predict
        prediction = model.predict(final_scaled)
        
        return jsonify({'price': round(float(prediction[0]), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)