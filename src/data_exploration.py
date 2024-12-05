import pandas as pd

# Load the dataset
df = pd.read_csv("data/Crop_recommendation.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset Info:")
print(df.info())

# Display summary statistics for numerical data
print("\nSummary Statistics:")
print(df.select_dtypes(include=['int64', 'float64']).describe())
