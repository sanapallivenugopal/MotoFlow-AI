import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="MotoFlow Pro AI", layout="wide")

# --- HEADER ---
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.markdown("### *AI-Driven Predictive Maintenance & Diagnostic Suite*")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Fleet Control Panel")
selected_bike = st.sidebar.selectbox("Select Vehicle ID", ["RE-GUERRILLA-450-01", "RE-HIM-450-09", "RE-INT-650-04"])
days_simulated = st.sidebar.slider("Forecast Period (Days)", 7, 30, 14)

# --- SYSTEM LOGIC ---
# Simulating real-time sensor data
def get_sensor_data():
    df = pd.DataFrame({
        'Day': range(1, 31),
        'Engine Temp (°C)': np.random.randint(85, 105, 30),
        'Vibration Level (Hz)': np.random.uniform(1.2, 5.5, 30),
        'Oil Pressure (PSI)': np.random.randint(40, 60, 30)
    })
    return df

data = get_sensor_data()

# --- DASHBOARD LAYOUT ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Fleet Mileage", "12,450 km", "+120km Today")
with col2:
    st.metric("System Health", "94%", "-2% Wear")
with col3:
    st.metric("Active Rentals", "8 / 10", "High Demand")

st.write("---")

# --- COMPLEX VISUALS ---
st.subheader("Vehicle Telemetry Analysis")
tab1, tab2 = st.tabs(["Engine Performance", "Predictive Risk Model"])

with tab1:
    fig = px.line(data, x='Day', y=['Engine Temp (°C)', 'Oil Pressure (PSI)'], 
                 title="Real-Time Sensor Feed", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.write("#### AI Probability of Part Failure")
    # Simulation of a maintenance prediction
    risk_data = pd.DataFrame({
        'Component': ['Brake Pads', 'Chain Drive', 'Engine Oil', 'Tires'],
        'Wear %':
    })
    fig2 = px.bar(risk_data, x='Component', y='Wear %', color='Wear %',
                 color_continuous_scale='Reds', range_y=)
    st.plotly_chart(fig2, use_container_width=True)
    
    st.warning("🚨 CRITICAL ALERT: Brake Pads on RE-GUERRILLA-450-01 exceed 80% wear threshold.")

# --- FOOTER ---
st.info("MotoFlow AI is currently processing live telemetry via simulated MQTT protocols.")
