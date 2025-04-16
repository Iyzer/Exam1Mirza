import streamlit as st
import pandas as pd

# Define the URL to the CSV file
file_url = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/auto.csv"

# Define the custom headers
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Load the dataset directly from the URL with custom headers
df = pd.read_csv(file_url, names=headers, header=0)  # Set header=0 to skip the first row in the file

# Display the first few rows of the dataset
st.write("Here is the dataset:")
st.write(df.head())

# Now you can proceed with data cleaning, transformation, etc.
# For example, handling missing values:
df.fillna(df.mean(), inplace=True)
st.write("Data after filling missing values:")
st.write(df.head())




