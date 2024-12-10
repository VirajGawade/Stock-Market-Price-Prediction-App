import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# Fetch stock data
def fetch_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(start=start_date, end=end_date)
    return data['Close'].values  # Returning closing prices as NumPy array

# Predict stock price
def predict_stock_price(stock_symbol, start_date, end_date):
    # Fetch data
    data = fetch_stock_data(stock_symbol, start_date, end_date)
    
    # Check if there's enough data
    if len(data) < 60:
        return {"error": "Not enough data to make predictions. Need at least 60 days of stock data."}

    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))

    # Prepare data for prediction
    X_test = []
    for i in range(60, len(scaled_data)):
        X_test.append(scaled_data[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Load model
    model = load_model("stock_prediction_model.h5")
    
    # Make predictions
    predicted_prices = model.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted_prices)

    # Return the last predicted price
    return {"predicted_price": predicted_prices[-1][0]}
