# app.py
import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('forecasting_co2_emmision.pkl')

st.set_page_config(page_title="CO₂ Emission Predictor", layout="centered")
st.title("🌍 CO₂ Emissions per Capita Predictor")

st.markdown("Enter feature values below to estimate carbon emissions per capita:")

# Selected features (based on RFECV)
selected_features = ['cereal_yield', 'gni_per_cap', 'en_per_cap',
                     'pop_urb_aggl_perc', 'prot_area_perc',
                     'pop_growth_perc', 'urb_pop_growth_perc']

# Feature input sliders / boxes
inputs = []
inputs.append(st.number_input('Cereal Yield (kg/ha)', value=3000.0))
inputs.append(st.number_input('GNI per Capita (Atlas $)', value=4000.0))
inputs.append(st.number_input('Energy Use per Capita (kg oil eq.)', value=1000.0))
inputs.append(st.slider('Population in Urban Agglomerations >1M (%)', 0.0, 100.0, 50.0))
inputs.append(st.slider('Protected Areas (% of land area)', 0.0, 100.0, 10.0))
inputs.append(st.slider('Population Growth (annual %)', -5.0, 10.0, 1.5))
inputs.append(st.slider('Urban Population Growth (annual %)', -5.0, 10.0, 2.0))

# Predict button
if st.button("🔍 Predict CO₂ per Capita"):
    features_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(features_array)[0]
    st.success(f"📈 Predicted CO₂ Emissions per Capita: **{prediction:.2f} metric tons**")
