from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the House Price Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data['features'])])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
