import yfinance as yf
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Function to fetch stock data from Yahoo Finance
def fetch_stock_data(stock_symbol, start_date, end_date):
    print(f"Fetching data for {stock_symbol} from {start_date} to {end_date}...")
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    if data.empty:
        raise ValueError(f"No data found for {stock_symbol} in the given date range.")
    return data

# Function to prepare the data
def prepare_data(data, sequence_length):
    x, y = [], []
    for i in range(len(data) - sequence_length):
        x.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(x), np.array(y)

# Parameters for stock data
stock_symbol = "AAPL"  # Replace with desired stock symbol
start_date = "2018-01-01"
end_date = "2022-01-01"

# Fetch stock data
df = fetch_stock_data(stock_symbol, start_date, end_date)
close_prices = df['Close'].values.reshape(-1, 1)

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_prices)

# Sequence length for LSTM
sequence_length = 60

# Prepare the data
x, y = prepare_data(scaled_data, sequence_length)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Build the LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=32, epochs=10)  # Adjust epochs as needed

# Save the model
model.save('stock_prediction_model.h5')

# Save the scaler for later use
import joblib
joblib.dump(scaler, 'scaler.pkl')

print(f"Model training complete and saved as 'stock_prediction_model.h5'")
