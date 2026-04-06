import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="MotoFlow Pro AI", layout="wide")

# 2. Main Heading
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.markdown("#### *AI-Driven Predictive Maintenance & Diagnostic Suite*")

# 3. Sidebar Selection
st.sidebar.header("Fleet Control Panel")
selected_bike = st.sidebar.selectbox("Select Vehicle ID", ["RE-GUERRILLA-450-01", "RE-HIMALAYAN-450-05"])

# 4. Core Metrics Display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Mileage", value="12,450 km")
with col2:
    st.metric(label="System Health", value="94%")
with col3:
    st.metric(label="Risk Level", value="LOW")

st.write("---")

# 5. Charts and Visuals
tab1, tab2 = st.tabs(["📊 Telemetry Feed", "⚙️ Part Wear Analysis"])

with tab1:
    # Creating a simple data table for the line chart
    chart_values = np.random.randint(low=70, high=105, size=(20, 2))
    chart_df = pd.DataFrame(data=chart_values, columns=["Engine Temp", "Oil Pressure"])
    st.line_chart(data=chart_df)

with tab2:
    # Using simple lists for the bar chart to avoid Dictionary Syntax Errors
    names_list = ["Brake Pads", "Chain Drive", "Engine Oil", "Tires"]
    wear_list =
    
    # Building the Bar Chart with Plotly Express
    fig = px.bar(x=names_list, y=wear_list, color=wear_list, color_continuous_scale="Reds")
    fig.update_layout(xaxis_title="Vehicle Component", yaxis_title="Wear Percentage (%)")
    st.plotly_chart(figure_or_data=fig, use_container_width=True)

# 6. Automated Safety Alert
highest_wear = max(wear_list)
if highest_wear > 80:
    st.error(f"🚨 CRITICAL ALERT: High wear detected on {selected_bike}. Service Brakes Immediately.")
