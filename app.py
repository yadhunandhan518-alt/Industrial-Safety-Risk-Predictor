import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
import time

st.set_page_config(
    page_title="SafeGuard AI",
    page_icon="🌍",
    layout="wide"
)

# =========================
# SPLASH SCREEN
# =========================

if "loaded" not in st.session_state:

    st.markdown(
        """
        <h1 style='text-align:center;'>
        🌍 SafeGuard AI
        </h1>

        <h4 style='text-align:center;color:gray;'>
        Industrial Risk Prediction & Monitoring System
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.image("globe.gif", width=350)

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.03)
        progress.progress(i + 1)

    st.session_state.loaded = True
    st.rerun()

# =========================
# DASHBOARD
# =========================

st.title("🏭 SafeGuard AI Dashboard")

st.markdown("---")

# Sample Training Data

data = pd.DataFrame({
    'Temperature':[25,40,60,30,55,70,35,50],
    'Humidity':[40,60,85,50,90,95,55,80],
    'Gas':[50,150,400,80,350,500,100,300],
    'Vibration':[2,5,18,4,15,20,6,14],
    'Risk':[0,1,2,0,2,2,1,2]
})

X = data[['Temperature','Humidity','Gas','Vibration']]
y = data['Risk']

model = RandomForestClassifier()
model.fit(X, y)

st.sidebar.header("⚙ Enter Parameters")

temp = st.sidebar.slider(
    "Temperature (°C)",
    0,
    100,
    40
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    0,
    100,
    60
)

gas = st.sidebar.slider(
    "Gas Level (ppm)",
    0,
    500,
    150
)

vibration = st.sidebar.slider(
    "Machine Vibration",
    0,
    25,
    5
)

prediction = model.predict(
    [[temp, humidity, gas, vibration]]
)[0]

risk_labels = {
    0:"🟢 LOW",
    1:"🟡 MEDIUM",
    2:"🔴 HIGH"
}

st.subheader("📊 Prediction Result")

if prediction == 0:
    st.success(
        f"Risk Level: {risk_labels[prediction]}"
    )

elif prediction == 1:
    st.warning(
        f"Risk Level: {risk_labels[prediction]}"
    )

else:
    st.error(
        f"Risk Level: {risk_labels[prediction]}"
    )

# INPUT DATA

st.subheader("📈 Current Inputs")

df = pd.DataFrame({
    "Parameter":[
        "Temperature",
        "Humidity",
        "Gas",
        "Vibration"
    ],
    "Value":[
        temp,
        humidity,
        gas,
        vibration
    ]
})

st.bar_chart(df.set_index("Parameter"))

# GLOBAL MONITORING GLOBE

st.subheader("🌍 Global Industrial Monitoring")

fig = go.Figure(go.Scattergeo(
    lon=[77.59, -74.00, 139.69],
    lat=[12.97, 40.71, 35.68],
    mode='markers+text',
    text=[
        'Bangalore Plant',
        'New York Plant',
        'Tokyo Plant'
    ],
    marker=dict(
        size=[18,18,18]
    )
))

fig.update_geos(
    projection_type="orthographic",
    showland=True,
    landcolor="rgb(40,40,40)",
    showocean=True,
    oceancolor="rgb(0,60,120)"
)

fig.update_layout(
    height=600,
    margin=dict(
        l=0,
        r=0,
        t=0,
        b=0
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.caption(
    "SafeGuard AI © 2026 | Industrial Safety Monitoring Platform"
)
