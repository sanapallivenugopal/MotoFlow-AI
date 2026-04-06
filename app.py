import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Setup
st.set_page_config(page_title="MotoFlow Pro AI", layout="wide")

# 2. Header
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.markdown("#### *AI-Driven Predictive Maintenance & Diagnostic Suite*")
st.write("---")

# 3. Sidebar
st.sidebar.header("Fleet Control Panel")
bike_list = ["RE-GUERRILLA-450-01", "RE-HIM-450-09", "RE-INT-650-04"]
selected_bike = st.sidebar.selectbox("Select Vehicle ID", bike_list)

# 4. Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Total Mileage", "12,450 km")
c2.metric("System Health", "94%")
c3.metric("Risk Level", "LOW")

# 5. Charts
st.write("###")
t1, t2 = st.tabs(["Telemetry", "Component Wear"])

with t1:
    # Line Chart
    df_line = pd.DataFrame(np.random.randint(40,100,size=(24, 2)), columns=['Engine Temp', 'Oil Pressure'])
    st.line_chart(df_line)

with t2:
    # Bar Chart - FIXED DATA STRUCTURE
    wear_data = {
        'Component': ['Brakes', 'Chain', 'Oil', 'Tires', 'Battery'],
        'WearPercentage':
    }
    df_bar = pd.DataFrame(wear_data)
    fig2 = px.bar(df_bar, x='Component', y='WearPercentage', color='WearPercentage', color_continuous_scale='Reds')
    st.plotly_chart(fig2, use_container_width=True)

# 6. Alerts
if any(df_bar['WearPercentage'] > 80):
    st.error(f"🚨 ALERT: High wear detected on {selected_bike}. Check Brake System.")
