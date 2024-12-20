from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)
CORS(app)

# Load diabetes dataset with tab delimiter
data = pd.read_csv('data/diabetes.csv', delimiter='\t')

# Clean up column names if necessary (remove any leading/trailing whitespace)
data.columns = data.columns.str.strip()  

# Preprocess data
X = data.drop('Outcome', axis=1)  # Features
y = data['Outcome']                # Target variable

# Split data into training and testing sets (optional for this example)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the trained model (if not already saved)
joblib.dump(model, 'scripts/logistic_regression.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML page

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json

        # Prepare input for prediction
        model_input = [[
            input_data['pregnancies'],
            input_data['glucose'],
            input_data['bloodpressure'],
            input_data['skinthickness'],
            input_data['insulin'],
            input_data['bmi'],
            input_data['diabetespedigreefunction'],  # Ensure this is included
            input_data['age']
        ]]

        prediction = model.predict(model_input)

        return jsonify({
            'prediction': int(prediction[0]),
            'message': 'Prediction made successfully'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)