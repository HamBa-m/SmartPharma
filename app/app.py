import streamlit as st
import pandas as pd

# Sample data - Replace with your LSTM model output
data = {
    'Product Class': ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6'],
    'City': ['City 1', 'City 2', 'City 3', 'City 4', 'City 5', 'City 6'],
    'Quantity': [100, 150, 200, 250, 300, 350],
    'Month': ['January', 'February', 'March', 'April', 'May', 'June']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Medicaments Delivery Schedule')
st.write('This application shows the delivery schedule for different product classes.')

# Filters
st.sidebar.header('Filters')
product_class = st.sidebar.multiselect('Product Class', df['Product Class'].unique())
city = st.sidebar.multiselect('City', df['City'].unique())
month = st.sidebar.multiselect('Month', df['Month'].unique())

# Filter data
filtered_df = df[(df['Product Class'].isin(product_class)) & (df['City'].isin(city)) & (df['Month'].isin(month))]

# Display the data
st.write('### Delivery Commands')
st.dataframe(filtered_df)
