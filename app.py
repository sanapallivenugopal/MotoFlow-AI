import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration (Sets the professional look)
st.set_page_config(page_title="MotoFlow Pro AI", layout="wide", initial_sidebar_state="expanded")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #374151; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.markdown("#### *AI-Driven Predictive Maintenance & Diagnostic Suite*")
st.write("---")

# 4. Sidebar Controls
st.sidebar.image("https://img.icons8.com/ios-filled/100/ffffff/motorcycle.png")
st.sidebar.header("Fleet Control Panel")
selected_bike = st.sidebar.selectbox("Select Vehicle ID", ["RE-GUERRILLA-450-01", "RE-HIM-450-09", "RE-INT-650-04"])
st.sidebar.success(f"Connected to {selected_bike}")

# 5. Core Metrics (Top Row)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Mileage", "12,450 km", "↑ 120km")
with col2:
    st.metric("System Health", "94%", "Stable")
with col3:
    st.metric("Risk Level", "LOW", "Optimal")
with col4:
    st.metric("Active Rentals", "8 / 10", "High Demand")

st.write("###") # Spacing

# 6. Technical Charts (Middle Row)
tab1, tab2 = st.tabs(["📊 Real-Time Telemetry", "⚙️ Component Wear"])

with tab1:
    # Simulating sensor data for the graph
    chart_data = pd.DataFrame({
        'Hour': range(1, 25),
        'Engine Temp (°C)': np.random.randint(85, 105, 24),
        'Oil Pressure (PSI)': np.random.randint(40, 60, 24)
    })
    fig = px.line(chart_data, x='Hour', y=['Engine Temp (°C)', 'Oil Pressure (PSI)'], 
                 template="plotly_dark", color_discrete_sequence=['#ff4b4b', '#1f77b4'])
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Component health analysis
    risk_df = pd.DataFrame({
        'Component': ['Brake Pads', 'Chain Drive', 'Engine Oil', 'Tires', 'Battery'],
        'Wear %':
    })
    fig2 = px.bar(risk_df, x='Component', y='Wear %', color='Wear %', 
                 color_continuous_scale='Reds', template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

# 7. Predictive Alerts (Bottom)
st.write("---")
st.subheader("⚠️ Intelligence Alerts")
if 82 in risk_df.values:
    st.error(f"**CRITICAL:** {selected_bike} Brake Pads exceed 80% wear threshold. Schedule maintenance immediately.")
else:
    st.info("All systems within safe operating parameters.")
