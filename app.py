from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML frontend

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the frontend
    data = request.form.to_dict()
    try:
        features = [
            float(data['MedInc']),
            float(data['HouseAge']),
            float(data['AveRooms']),
            float(data['AveBedrms']),
            float(data['Population']),
            float(data['AveOccup']),
            float(data['Latitude']),
            float(data['Longitude']),
        ]

        # Make prediction
        prediction = model.predict([np.array(features)])
        return jsonify({'prediction': prediction[0]})
    except KeyError as e:
        return jsonify({'error': f"Missing feature: {e}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
