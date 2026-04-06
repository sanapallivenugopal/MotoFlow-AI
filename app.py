import streamlit as st

st.set_page_config(page_title="MotoFlow AI", page_icon="🏍️")

st.title("🏍️ MotoFlow: Smart Bike Health Monitor")
st.subheader("Predictive Maintenance for Long-Distance Riders")

# Input Section
bike_model = st.selectbox("Select Your Bike", ["Royal Enfield Guerrilla 450", "Himalayan 450", "Interceptor 650"])
mileage = st.number_input("Current Odometer (km)", value=5000)
last_service = st.number_input("km since last service", value=1000)

# Health Logic
health_score = 100 - (last_service / 100)
if health_score < 50:
    status, color = "🔴 CRITICAL: Service Now", "red"
elif health_score < 80:
    status, color = "🟡 WARNING: Checkup Soon", "orange"
else:
    status, color = "🟢 HEALTHY: Ready to Ride", "green"

# Results
st.metric(label="Vehicle Health Score", value=f"{health_score}%")
st.markdown(f"### Status: :{color}[{status}]")

st.write("---")
st.write("### Recommended Maintenance:")
if health_score < 80:
    st.write("- Check Oil Levels\n- Inspect Chain Tension\n- Verify Brake Pad Wear")
else:
    st.write("- All systems operational. Ride safe!")
  
