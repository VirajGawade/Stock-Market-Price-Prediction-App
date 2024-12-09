from flask import Flask, request, jsonify
import yfinance as yf
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = "stock_prediction_model.h5"
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


def fetch_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(start=start_date, end=end_date)
    return data


def predict_stock_price(stock_symbol, start_date, end_date):
    try:
        # Fetch the stock data
        data = fetch_stock_data(stock_symbol, start_date, end_date)

        # Ensure we have enough data
        if data.empty:
            return {"error": "No data available for the given date range"}

        # Prepare the data for prediction
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1, 1))
        X_test = np.array([scaled_data[-60:]])  # Use the last 60 days for prediction
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

        # Make the prediction
        prediction = model.predict(X_test)
        predicted_price = scaler.inverse_transform(prediction)[0][0]
        return {"prediction": float(predicted_price)}

    except Exception as e:
        return {"error": str(e)}


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Stock Prediction API!"})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running"})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    stock_symbol = data.get("stock_symbol")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    # Validate inputs
    if not all([stock_symbol, start_date, end_date]):
        return jsonify({"error": "Missing required parameters: stock_symbol, start_date, end_date"}), 400

    # Make prediction
    result = predict_stock_price(stock_symbol, start_date, end_date)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
