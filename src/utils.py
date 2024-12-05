import pandas as pd

# Function to load the dataset
def load_data(filepath):
    return pd.read_csv(filepath)

# Function to extract lists of values for a specific factor
def get_factor_lists(df, factor, crop_types):
    return [df[df['label'] == crop][factor] for crop in crop_types]
