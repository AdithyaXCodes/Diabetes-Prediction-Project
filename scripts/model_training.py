import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset with tab delimiter
data = pd.read_csv('data/diabetes.csv', delimiter='\t')

# Clean up column names if necessary (remove any leading/trailing whitespace)
data.columns = data.columns.str.strip()  

# Define features and target variable
X = data.drop('Outcome', axis=1)  # Features
y = data['Outcome']                # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the trained model for later use
joblib.dump(model, 'scripts/logistic_regression.pkl')

print("Model training completed successfully and saved.")