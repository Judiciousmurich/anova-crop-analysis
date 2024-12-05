import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("data/Crop_recommendation.csv")

# Setting the aesthetic style of the plots
sns.set(style="whitegrid")

# Creating visualizations for Temperature, Humidity, and Rainfall
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Temperature Distribution
sns.histplot(df['temperature'], kde=True, color="skyblue", ax=axes[0])
axes[0].set_title('Temperature Distribution')

# Humidity Distribution
sns.histplot(df['humidity'], kde=True, color="olive", ax=axes[1])
axes[1].set_title('Humidity Distribution')

# Rainfall Distribution
sns.histplot(df['rainfall'], kde=True, color="gold", ax=axes[2])
axes[2].set_title('Rainfall Distribution')

# Save the plots
plt.tight_layout()
plt.savefig("results/distributions.png")
plt.show()
