import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Reading the data from the URL
filename = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/auto.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(filename, names=headers)

# Replace "?" with NaN
df.replace("?", np.nan, inplace=True)

# Handling missing data
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore = df['bore'].astype('float').mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)

mean_stroke = df["stroke"].astype(float).mean()
df["stroke"].replace(np.nan, mean_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

df["num-of-doors"].replace(np.nan, "four", inplace=True)
df.dropna(subset=["price"], axis=0, inplace=True)

# Data type correction
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Transforming mpg to L/100km for city and highway
df['city-L/100km'] = 235 / df["city-mpg"]
df["highway-L/100km"] = 235 / df["highway-mpg"]
df.drop("highway-mpg", axis=1, inplace=True)

# Normalize selected columns
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()

# Streamlit App UI
st.title('Car Data Analysis')

st.subheader("Cleaned Data Preview:")
st.dataframe(df.head())

st.subheader("Missing Data Visualization:")
missing_data = df.isnull().sum()
st.bar_chart(missing_data)

st.subheader("Data Transformation Visualizations:")

# Plot for city-L/100km transformation
st.subheader("City MPG to L/100km")
fig, ax = plt.subplots()
ax.scatter(df['city-mpg'], df['city-L/100km'])
ax.set_title('City MPG to L/100km')
ax.set_xlabel('City MPG')
ax.set_ylabel('City L/100km')
st.pyplot(fig)

# Plot for normalized features: length and width
st.subheader("Normalized Length and Width")
fig2, ax2 = plt.subplots()
ax2.scatter(df['length'], df['width'])
ax2.set_title('Normalized Length vs Width')
ax2.set_xlabel('Normalized Length')
ax2.set_ylabel('Normalized Width')
st.pyplot(fig2)

# You can also visualize other parts of the data or any additional analysis you want to include.
