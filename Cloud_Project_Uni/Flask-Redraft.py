from flask import Flask, jsonify, request
from StockPrediction import fetch_stock_data, predict_stock_price
import numpy as np


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Stock Prediction API!"})

@app.route('/health')
def health_check():
    return jsonify({"status": "API is running"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    stock_symbol = data.get("stock_symbol")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    try:
        # Call the stock price prediction function
        prediction = predict_stock_price(stock_symbol, start_date, end_date)
        
        # Ensure the prediction is properly extracted and converted
        if isinstance(prediction, dict):  # Handle if the model returns a dict
            prediction_value = prediction.get("value", 0)  # Adjust based on actual structure
            prediction = float(prediction_value)
        elif hasattr(prediction, "item"):  # Handle NumPy scalars
            prediction = prediction.item()

        return jsonify({"prediction": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
