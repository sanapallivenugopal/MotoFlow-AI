import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PRO UI CONFIGURATION ---
st.set_page_config(page_title="MotoFlow Pro AI", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #3b82f6; }
    [data-testid="stSidebar"] { background-color: #111827; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.markdown("#### *Next-Gen Predictive Maintenance & Telemetry Suite*")
st.write("---")

# --- 3. SIDEBAR ---
st.sidebar.header("Global Fleet Control")
bike_id = st.sidebar.selectbox("Active Vehicle", ["RE-GUERRILLA-450-01", "RE-HIMALAYAN-450-05", "RE-INT-650-04"])
st.sidebar.info(f"Connected to ECU: {bike_id}")
st.sidebar.write("---")
st.sidebar.button("Refresh Telemetry Feed")

# --- 4. METRICS ---
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

# --- 5. DATA VISUALIZATION ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("📊 Live Engine Telemetry (24h)")
    time_steps = np.arange(24)
    temp_vals = np.random.randint(85, 105, 24)
    pressure_vals = np.random.randint(40, 60, 24)

    telemetry_df = pd.DataFrame({
        "Hour": time_steps,
        "Temp": temp_vals,
        "PSI": pressure_vals
    })

    fig_line = px.line(
        telemetry_df,
        x="Hour",
        y=["Temp", "PSI"],
        template="plotly_dark"
    )

    fig_line.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig_line, use_container_width=True)

with col_b:
    st.subheader("⚙️ Part Wear Analysis")
    parts = ["Brakes", "Chain", "Oil", "Tires"]

    # ✅ FIXED LINE
    wear_levels = np.random.randint(40, 95, 4)

    fig_bar = px.bar(
        x=parts,
        y=wear_levels,
        color=wear_levels,
        color_continuous_scale="Reds",
        template="plotly_dark"
    )

    fig_bar.update_layout(
        xaxis_title="Component",
        yaxis_title="Wear %",
        showlegend=False
    )

    st.plotly_chart(fig_bar, use_container_width=True)

# --- 6. AI ALERTS ---
st.write("---")

if max(wear_levels) > 80:
    st.error(f"⚠️ CRITICAL ALERT: {bike_id} has high wear detected. Immediate maintenance required.")
else:
    st.success("✅ All components are in safe condition.")
