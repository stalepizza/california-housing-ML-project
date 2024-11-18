California Housing Price Prediction
Welcome to the California Housing Price Prediction project! 🚀

Overview
This project aims to predict the median house prices in California using various features from the California Housing dataset. It's a comprehensive exercise in data preprocessing, model training, evaluation, and deployment using Python and Flask.

Table of Contents
Overview

Project Structure

Installation

Usage

Model Deployment

Contributing

License

Contact

Project Structure
Here’s a quick glance at the project structure:

california-housing-ML-project/
│
├── notebooks/
│   ├── 01_environment_setup.ipynb
│   ├── 02_data_loading_exploration.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
│
├── app.py
├── linear_regression_model.pkl
├── requirements.txt
├── Procfile
└── README.md
Installation
To run this project locally, follow these steps:

Clone the repository:

bash
git clone https://github.com/stalepizza/california-housing-ML-project.git
cd california-housing-ML-project
Install dependencies:

bash
pip install -r requirements.txt
Start Jupyter Notebook:

bash
jupyter notebook
Run the notebooks sequentially to see the steps involved in data preprocessing, model training, and evaluation.

Usage
Start the Flask App:

bash
python app.py
Make Predictions:

You can use tools like curl or Postman to interact with the API.

Example curl command:

bash
curl -X POST -H "Content-Type: application/json" -d '{"features": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]}' http://127.0.0.1:5000/predict
Model Deployment
You can deploy this Flask app on platforms like Heroku, Render, or Google Cloud Platform. The Procfile and requirements.txt are included to help with deployment.

Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request. Let's make this project even better together!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or feedback, feel free to reach out:

Email: prishaprakash9903@gmail.com

GitHub: stalepizza

Happy Coding! 🎉
