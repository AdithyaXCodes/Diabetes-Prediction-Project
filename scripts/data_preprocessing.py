import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset with tab delimiter
data = pd.read_csv('data/diabetes.csv', delimiter='\t')

# Inspect data to check if it loaded correctly
print("DataFrame Shape:", data.shape)  # Show shape of DataFrame
print("Column Names:", data.columns.tolist())  # Show all column names

# Clean up column names if necessary (remove any leading/trailing whitespace)
data.columns = data.columns.str.strip()  

# Define features and target variable
X = data.drop('Outcome', axis=1)  # Features
y = data['Outcome']                # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data for later use (optional)
X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Data preprocessing completed successfully.")