import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PRO UI CONFIGURATION ---
st.set_page_config(page_title="MotoFlow Pro AI", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for that "High-End" Enterprise Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #3b82f6; }
    [data-testid="stSidebar"] { background-color: #111827; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER & BRANDING ---
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.markdown("#### *Next-Gen Predictive Maintenance & Telemetry Suite*")
st.write("---")

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.header("Global Fleet Control")
bike_id = st.sidebar.selectbox("Active Vehicle", ["RE-GUERRILLA-450-01", "RE-HIMALAYAN-450-05", "RE-INT-650-04"])
st.sidebar.info(f"Connected to ECU: {bike_id}")
st.sidebar.write("---")
st.sidebar.button("Refresh Telemetry Feed")

# --- 4. REAL-TIME METRICS ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Total Fleet Mileage", value="12,450 km", delta="120 km Today")
with m2:
    st.metric(label="System Health Score", value="94%", delta="-2% Wear")
with m3:
    st.metric(label="Risk Assessment", value="LOW", delta="Optimal")
with m4:
    st.metric(label="Active Sessions", value="8 / 10", delta="High Demand")

st.write("###")

# --- 5. COMPLEX DATA VISUALIZATION ---
col_a, col_b = st.columns()

with col_a:
    st.subheader("📊 Live Engine Telemetry (24h)")
    # Complex random data generation for Python 3.14
    time_steps = np.arange(24)
    temp_vals = np.random.randint(85, 105, 24)
    pressure_vals = np.random.randint(40, 60, 24)
    
    telemetry_df = pd.DataFrame({"Hour": time_steps, "Temp": temp_vals, "PSI": pressure_vals})
    
    fig_line = px.line(telemetry_df, x="Hour", y=["Temp", "PSI"], 
                      template="plotly_dark", color_discrete_sequence=["#ef4444", "#3b82f6"])
    fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_line, use_container_width=True)

with col_b:
    st.subheader("⚙️ Part Wear Analysis")
    parts = ["Brakes", "Chain", "Oil", "Tires"]
    wear_levels =
    
    fig_bar = px.bar(x=parts, y=wear_levels, color=wear_levels, 
                    color_continuous_scale="Reds", template="plotly_dark")
    fig_bar.update_layout(xaxis_title="Component", yaxis_title="Wear %", showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

# --- 6. AI PREDICTIVE ALERTS ---
st.write("---")
if max(wear_levels) > 80:
    st.error(f"⚠️ **CRITICAL PREDICTIVE ALERT:** {bike_id} shows excessive Brake Pad wear (82%). System recommends immediate replacement to avoid rotor damage.")
else:
    st.success("✅ AI Analysis: All hardware components are within safe operating thresholds.")
