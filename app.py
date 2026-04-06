import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="MotoFlow Pro AI", layout="wide")

# --- HEADER ---
st.title("🏍️ MotoFlow Pro: Enterprise Fleet Analytics")
st.write("---")

# --- AUTO GENERATE 20+ BIKES ---
brands = ["RE", "KAWASAKI", "YAMAHA", "DUCATI", "BMW", "SUZUKI", "HONDA", "APRILIA", "KTM", "TRIUMPH"]

models = {
    "RE": ["CLASSIC350", "HIMALAYAN450", "GUERRILLA450"],
    "KAWASAKI": ["ZX10R", "NINJA650"],
    "YAMAHA": ["R1", "R15"],
    "DUCATI": ["PANIGALEV4"],
    "BMW": ["S1000RR"],
    "SUZUKI": ["HAYABUSA"],
    "HONDA": ["CBR1000RR"],
    "APRILIA": ["RSV4"],
    "KTM": ["RC390"],
    "TRIUMPH": ["DAYTONA675"]
}

bikes = []
count = 1

for brand in brands:
    for model in models[brand]:
        bikes.append(f"{brand}-{model}-{count:02d}")
        count += 1

# Ensure at least 20 bikes
bikes = bikes[:25]

# --- SIDEBAR ---
bike_id = st.sidebar.selectbox("Select Bike", bikes)

# 🔥 UNIQUE SEED PER BIKE
seed = sum(ord(c) for c in bike_id)
np.random.seed(seed)

# --- METRICS ---
m1, m2, m3, m4 = st.columns(4)

mileage = np.random.randint(3000, 25000)
health = np.random.randint(60, 100)
sessions = np.random.randint(1, 10)

if health > 85:
    risk = "LOW"
elif health > 70:
    risk = "MEDIUM"
else:
    risk = "HIGH"

with m1:
    st.metric("Mileage", f"{mileage} km")
with m2:
    st.metric("Health", f"{health}%")
with m3:
    st.metric("Risk", risk)
with m4:
    st.metric("Sessions", sessions)

st.write("###")

# --- TELEMETRY ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Engine Telemetry")

    hours = np.arange(24)
    temp = np.random.randint(80, 110, 24)
    psi = np.random.randint(30, 60, 24)

    df = pd.DataFrame({
        "Hour": hours,
        "Temp": temp,
        "PSI": psi
    })

    fig = px.line(df, x="Hour", y=["Temp", "PSI"], template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# --- WEAR ANALYSIS ---
with col2:
    st.subheader("⚙️ Wear Analysis")

    parts = ["Brakes", "Chain", "Oil", "Tires"]
    wear_levels = np.random.randint(30, 100, 4)

    fig2 = px.bar(
        x=parts,
        y=wear_levels,
        color=wear_levels,
        color_continuous_scale="Reds",
        template="plotly_dark"
    )

    st.plotly_chart(fig2, use_container_width=True)

# --- ALERT SYSTEM ---
st.write("---")

problem_parts = ["Brakes", "Chain", "Oil", "Tires"]
max_wear = max(wear_levels)
problem = problem_parts[np.argmax(wear_levels)]

if max_wear > 85:
    st.error(f"⚠️ CRITICAL: {bike_id} → {problem} wear at {max_wear}%")
elif max_wear > 65:
    st.warning(f"⚠️ WARNING: {bike_id} → {problem} wear at {max_wear}%")
else:
    st.success(f"✅ {bike_id} is in excellent condition")

# --- EXTRA: BIKE-SPECIFIC ISSUE PANEL ---
issues = [
    "Brake pad wear",
    "Chain slack issue",
    "Oil degradation",
    "Tire pressure imbalance",
    "Battery drop",
    "Overheating risk",
    "No major issues"
]

issue = issues[seed % len(issues)]

st.sidebar.write("### ⚙️ Detected Issue")
st.sidebar.write(issue)
