import pandas as pd

# Path to your CSV file
file_path = 'data/diabetes.csv'

try:
    # Attempt to read the CSV file
    data = pd.read_csv(file_path)
    print("File read successfully!")
    print(data.head())  # Display the first few rows of the dataframe
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: There was a problem parsing the CSV file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")