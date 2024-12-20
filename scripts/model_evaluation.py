import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the test data (you can also split your original dataset again if needed)
# For this example, we'll assume you want to evaluate on the same data
data = pd.read_csv('data/diabetes.csv', delimiter='\t')
data.columns = data.columns.str.strip()  # Clean up column names

# Define features and target variable
X = data.drop('Outcome', axis=1)  # Features
y = data['Outcome']                # Target variable

# Load the trained model
model = joblib.load('scripts/logistic_regression.pkl')

# Make predictions on the entire dataset or a specific test set if you have one
predictions = model.predict(X)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y, predictions))
print("\nClassification Report:")
print(classification_report(y, predictions))