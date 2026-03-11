from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML pipeline components
model = joblib.load("Random_Forest_model.joblib")
encoder = joblib.load("encoder.joblib")
scaler = joblib.load("scaler.joblib")

# Feature columns (must match training data)
NUM_COLS = [
    'hour','day','month','distance',
    'surge_multiplier','temperature',
    'humidity','pressure','is_rain'
]

CAT_COLS = [
    'source','destination','cab_type','name'
]

@app.route("/")
def home():
    return jsonify({"message": "Cab Price Prediction API is running"})


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        # Convert input to DataFrame
        input_df = pd.DataFrame([data])

        # Encode categorical features
        cat_encoded = encoder.transform(input_df[CAT_COLS])
        cat_encoded_df = pd.DataFrame(
            cat_encoded,
            columns=encoder.get_feature_names_out()
        )

        # Combine numerical + categorical
        num_df = input_df[NUM_COLS].reset_index(drop=True)
        final_df = pd.concat([cat_encoded_df, num_df], axis=1)

        # Scale
        final_scaled = scaler.transform(final_df)

        # Prediction
        prediction = model.predict(final_scaled)

        return jsonify({
            "predicted_price": float(prediction[0])
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)