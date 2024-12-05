from scipy.stats import f_oneway
import pandas as pd

# Load the dataset
df = pd.read_csv("data/Crop_recommendation.csv")

# Define crop types
crop_types = df['label'].unique()

# Function to perform ANOVA for a given factor
def perform_anova(factor):
    factor_lists = [df[df['label'] == crop][factor] for crop in crop_types]
    anova_result = f_oneway(*factor_lists)
    return anova_result

# Perform ANOVA for humidity
humidity_result = perform_anova('humidity')
print("ANOVA Results for Humidity:")
print(humidity_result)

# Perform ANOVA for rainfall
rainfall_result = perform_anova('rainfall')
print("\nANOVA Results for Rainfall:")
print(rainfall_result)

# Perform ANOVA for temperature
temperature_result = perform_anova('temperature')
print("\nANOVA Results for Temperature:")
print(temperature_result)

# Save results to a text file
with open("results/anova_results.txt", "w") as f:
    f.write("ANOVA Results for Humidity:\n")
    f.write(str(humidity_result) + "\n\n")
    f.write("ANOVA Results for Rainfall:\n")
    f.write(str(rainfall_result) + "\n\n")
    f.write("ANOVA Results for Temperature:\n")
    f.write(str(temperature_result) + "\n")
