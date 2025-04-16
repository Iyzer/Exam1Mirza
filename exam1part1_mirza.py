import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the URL to the CSV file
file_url = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/auto.csv"

# Define the custom headers
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Load the dataset directly from the URL with custom headers
df = pd.read_csv(file_url, names=headers, header=0)  # Set header=0 to skip the first row in the file

# Handle missing values by filling numeric columns with the mean
df.fillna(df.select_dtypes(include=['float64', 'int64']).mean(), inplace=True)

# Display the first few rows of the dataset
st.write("### Dataset Overview")
st.write(df.head())

# Basic statistical summary
st.write("### Statistical Summary")
st.write(df.describe())

# Visualize a correlation heatmap
st.write("### Correlation Heatmap")
# Select only numeric columns for the correlation matrix
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
corr = df[numeric_columns].corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
st.pyplot()

# Visualize distribution of 'horsepower'
st.write("### Distribution of Horsepower")
plt.figure(figsize=(8, 6))
sns.histplot(df['horsepower'].dropna(), kde=True, color='blue')
st.pyplot()

# Visualize the relationship between 'engine-size' and 'price'
st.write("### Engine Size vs Price")
plt.figure(figsize=(8, 6))
sns.scatterplot(x='engine-size', y='price', data=df)
st.pyplot()
