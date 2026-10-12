# Stock Market Price Prediction App

Group project (4 members) - MSc Big Data Science, Queen Mary University of London (2024).
Graded 14/15.

Predicts stock closing prices with an LSTM model and serves predictions through a
Flask REST API, containerised with Docker and deployed on Google Cloud using Kubernetes.

**Tech:** Python · TensorFlow/Keras · Pandas · NumPy · Flask · Docker · Kubernetes · Google Cloud

## My contribution
The team worked together on all parts of the project - data pipeline, LSTM model,
Flask API, and Docker/Kubernetes deployment on Google Cloud – coding jointly on one machine.

## How it works
1. Fetches historical stock price data using yfinance
2. Cleans and scales the data (MinMaxScaler) and trains an LSTM model
3. A Flask REST API serves predictions and supports CRUD operations (GET, POST, PUT, DELETE)
4. The app runs in a Docker container on a Kubernetes cluster on Google Cloud

## System Architecture
![System Architecture](https://github.com/user-attachments/assets/f8960847-e587-4efc-91b0-4c27fac68059)
*Note: the diagram shows Google Finance from the initial design; the final implementation uses yfinance.*

## Cloud Architecture
![Cloud Architecture](https://github.com/user-attachments/assets/6cd9e58a-c665-4186-99d9-99de415926df)

## Original repository
Forked from [19-Dee/Stock-Market-Price-Prediction-App](https://github.com/19-Dee/Stock-Market-Price-Prediction-App) (team repo).
