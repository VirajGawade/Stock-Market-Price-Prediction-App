import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import numpy as np

# Global constants
LOOK_BACK = 60
MODEL_PATH = "bilstm_model.h5"

def fetch_stock_data(stock_symbol, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance for a given symbol and date range.
    """
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        stock_data.reset_index(inplace=True)
        if stock_data.empty:
            return pd.DataFrame()
        return stock_data
    except Exception as e:
        raise Exception(f"Failed to fetch stock data: {str(e)}")


def create_dataset(data, look_back=LOOK_BACK):
    """
    Create a dataset for time series prediction.
    """
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:(i + look_back)])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)


def predict_stock_price(stock_data):
    """
    Predict stock prices using the trained BiLSTM model.
    """
    try:
        # Ensure the Close column exists
        if "Close" not in stock_data.columns:
            raise ValueError("Stock data must contain 'Close' column.")

        # Scale the data
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(stock_data["Close"].values.reshape(-1, 1))

        # Create the dataset
        X, _ = create_dataset(scaled_data, LOOK_BACK)
        X = X.reshape((X.shape[0], X.shape[1], 1))

        # Load the trained model
        model = load_model(MODEL_PATH)

        # Generate predictions
        predicted_prices = model.predict(X)
        predicted_prices = scaler.inverse_transform(predicted_prices)

        return predicted_prices
    except Exception as e:
        raise Exception(f"Prediction failed: {str(e)}")
