import streamlit as st
import pandas as pd
import numpy as np

# Title of the Streamlit app
st.title('Car Data Cleaning & Transformation')

# Load the dataset from URL or upload
st.sidebar.subheader('Upload your dataset')
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    # Read the dataset into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write(df.head())  # Show the first few rows of the data

    # Display the column headers
    st.subheader('Column Headers')
    st.write(df.columns)

    # Show data types of columns
    st.subheader('Data Types')
    st.write(df.dtypes)

    # Handle Missing Values
    st.subheader('Handle Missing Values')

    # Replace "?" with NaN
    df.replace("?", np.nan, inplace=True)

    # Show missing data count
    st.write("Missing data count:")
    missing_data = df.isnull().sum()
    st.write(missing_data)

    # Option to replace missing values
    replace_option = st.selectbox(
        'Choose column to replace missing values',
        df.columns
    )
    if replace_option:
        replacement_value = st.number_input(f"Enter replacement value for {replace_option}", value=0)
        df[replace_option].fillna(replacement_value, inplace=True)
        st.write(f"Missing values in {replace_option} replaced.")

    # Show the cleaned data after handling missing values
    st.subheader('Cleaned Data After Missing Value Treatment')
    st.write(df.head())

    # Data Normalization Section
    st.subheader('Data Normalization')

    # Option to normalize columns
    columns_to_normalize = st.multiselect(
        'Choose columns to normalize',
        df.columns
    )

    if columns_to_normalize:
        for column in columns_to_normalize:
            df[column] = df[column] / df[column].max()
        st.write('Normalized Data:')
        st.write(df[columns_to_normalize].head())
    
    # Data Standardization Section (like mpg to L/100km transformation)
    st.subheader('Data Transformation (Standardization)')

    if 'city-mpg' in df.columns:
        df['city-L/100km'] = 235 / df['city-mpg']
        st.write(df[['city-mpg', 'city-L/100km']].head())

    if 'highway-mpg' in df.columns:
        df['highway-L/100km'] = 235 / df['highway-mpg']
        st.write(df[['highway-mpg', 'highway-L/100km']].head())

# You can add more interactive functionalities, buttons for actions, etc.



