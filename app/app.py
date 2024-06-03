import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import random

# Load the data from the provided JSON file
data = pd.read_json('app/predictions.json')

# Streamlit app
st.title('Medicaments Delivery Schedule')
st.write('This application shows the delivery schedule for different product classes.')

# Extract unique product classes and cities from the data
product_classes = list(set(key.split('_')[1] for key in data.keys()))
cities = list(set(key.split('_')[0] for key in data.keys()))

# Filters
st.sidebar.header('Filters')
selected_product_classes = st.sidebar.multiselect('Product Class', product_classes)
selected_cities = st.sidebar.multiselect('City', cities)

# Function to extract data based on selected filters
def get_filtered_data(selected_product_classes, selected_cities):
    filtered_data = {}
    for key in data.keys():
        key_city, key_product = key.split('_')
        if (not selected_product_classes or key_product in selected_product_classes) and (not selected_cities or key_city in selected_cities):
            filtered_data[key] = data[key]
    return filtered_data

# Filter data based on selections
filtered_data = get_filtered_data(selected_product_classes, selected_cities)

# If no filters are selected, show 5 random results
if not selected_product_classes and not selected_cities:
    all_keys = list(data.keys())
    random_keys = random.sample(all_keys, 5)
    filtered_data = {key: data[key] for key in random_keys}

# Plotting function
def plot_data(filtered_data):
    if filtered_data:
        combined_df = pd.DataFrame(filtered_data)
        combined_df.columns = [f'{key.split("_")[0]} - {key.split("_")[1]}' for key in combined_df.columns]

        # Create a date range starting from the current month
        current_date = datetime.now()
        months = [current_date + timedelta(days=i*30) for i in range(len(combined_df))]
        combined_df.index = [month.strftime('%b %Y') for month in months]

        st.line_chart(combined_df)

# Plot the data
st.write('### Predicted Medicament Needs Over Time')
plot_data(filtered_data)

# Message generation function with color based on urgency
def generate_messages(filtered_data):
    messages = []
    current_date = datetime.now()
    months = [current_date + timedelta(days=i*30) for i in range(len(next(iter(filtered_data.values()))))]
    for key, predictions in filtered_data.items():
        key_city, key_product = key.split('_')
        for i, demand in enumerate(predictions):
            if demand > 0:
                adjusted_demand = int(demand + demand * 0.05)
                month_to_send = months[i] - timedelta(days=30)
                days_until_delivery = (month_to_send - current_date).days
                if days_until_delivery <= 30:
                    color = f'rgba(255, 0, 0, {1.5 - (days_until_delivery / 30):.2f})'
                else:
                    color = 'rgba(255, 255, 255, 0.4)'
                message = (f'<span style="color:{color};">'
                           f'Send {adjusted_demand:.2f} units of {key_product} to {key_city} '
                           f'in {month_to_send.strftime("%b %Y")}.</span>')
                messages.append(message)
    return messages

# Generate and display messages
st.write('### Delivery Instructions')
messages = generate_messages(filtered_data)
for msg in messages:
    st.markdown(msg, unsafe_allow_html=True)