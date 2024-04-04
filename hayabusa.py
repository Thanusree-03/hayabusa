import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Loading
# Assuming the data is stored in a CSV file named 'hayabusa_mission_data.csv'
data = pd.read_csv('hayabusa_mission_data.csv')

# Step 2: Data Exploration
# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Get basic statistics of numerical columns
print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Step 3: Visualization
# Example: Plotting a histogram of a numerical column
plt.figure(figsize=(8, 6))
plt.hist(data['column_name'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Column Name')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
