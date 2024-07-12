import streamlit as st
import requests
import numpy as np

# Define feature columns
feature_cols = ['GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3P Made', '3PA', 
                '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 
                'STL', 'BLK', 'TOV']

st.title('NBA Player Classification MPData TEST')

st.sidebar.header('Player Input Features')
st.sidebar.markdown('Please input the player features below:')

# Input fields for all features using sliders
input_features = {}
for feature in feature_cols:
    input_features[feature] = st.sidebar.slider(feature, min_value=0.0, max_value=1000.0, step=1.0)

input_data = {feature: input_features[feature] for feature in feature_cols}

# Prediction button
if st.sidebar.button('Predict'):
    try:
        response = requests.post("http://127.0.0.1:8080/api/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()['decision']
            st.write(f"### Prediction: {result}")
        else:
            st.write(f"### Error: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.write(f"### Connection error: {e}")

# For displaying example input data
example_data = {
    'GP': 82, 'MIN': 2500, 'PTS': 1500, 'FGM': 600, 'FGA': 1200,
    'FG%': 50, '3P Made': 200, '3PA': 500, '3P%': 40, 'FTM': 500,
    'FTA': 600, 'FT%': 83, 'OREB': 200, 'DREB': 500, 'REB': 700,
    'AST': 400, 'STL': 100, 'BLK': 50, 'TOV': 150
}

st.write('### Example Input Data:')
st.write(example_data)

st.write('### Actual Player Data:')
st.write('Please use the sidebar to input actual player data.')
