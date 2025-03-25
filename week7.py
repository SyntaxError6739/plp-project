import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Loading
try:
    # Load data from a CSV file
    data = pd.read_csv('data.csv')
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please ensure 'data.csv' is in the correct directory.")
    exit()

# Step 2: Data Exploration
print("\nFirst 5 rows of the data:")
print(data.head())

print("\nData Information:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# Step 3: Basic Data Analysis
# Example: Count occurrences in a categorical column
if 'Category' in data.columns:
    print("\nCategory Counts:")
    print(data['Category'].value_counts())

# Example: Find the mean of a numerical column
if 'Value' in data.columns:
    mean_value = data['Value'].mean()
    print(f"\nAverage Value: {mean_value}")

# Step 4: Data Visualization
# Visualization: Histogram of 'Value'
if 'Value' in data.columns:
    plt.hist(data['Value'], bins=20, color='skyblue')
    plt.title("Distribution of 'Value'")
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Visualization: Pie chart for 'Category'
if 'Category' in data.columns:
    category_counts = data['Category'].value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen'])
    plt.title("Category Distribution")
    plt.show()

# Findings and Observations
# Example: Insights based on sample data exploration
print("\nFindings and Observations:")
print("1. The dataset contains {} rows and {} columns.".format(data.shape[0], data.shape[1]))
if 'Value' in data.columns:
    print(f"2. The average 'Value' is {mean_value}.")
if 'Category' in data.columns:
    print("3. Categories are distributed as shown in the pie chart.")

