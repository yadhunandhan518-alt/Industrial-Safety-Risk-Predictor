import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Industrial Safety Risk Predictor")


st.title("🌍 SafeGuard AI")
st.caption("Industrial Risk Prediction & Monitoring System")
import time

if "intro" not in st.session_state:

    st.markdown("""
    <div style='text-align:center;padding-top:100px'>
        <h1>🌍 SafeGuard AI</h1>
        <h3>Industrial Risk Prediction & Monitoring System</h3>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Rotating_earth_%28large%29.gif/512px-Rotating_earth_%28large%29.gif",
        width=350
    )

    st.progress(100)

    time.sleep(3)

    st.session_state.intro = True
    st.rerun()

st.title("🏭 Industrial Safety Risk Predictor")

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
model.fit(X,y)

st.sidebar.header("Enter Parameters")

temp = st.sidebar.slider("Temperature (°C)",0,100,40)
humidity = st.sidebar.slider("Humidity (%)",0,100,60)
gas = st.sidebar.slider("Gas Level (ppm)",0,500,150)
vibration = st.sidebar.slider("Machine Vibration",0,25,5)

prediction = model.predict([[temp,humidity,gas,vibration]])[0]

risk_labels = {
    0:"🟢 LOW",
    1:"🟡 MEDIUM",
    2:"🔴 HIGH"
}

st.subheader("Prediction Result")
st.success(f"Risk Level: {risk_labels[prediction]}")

if prediction == 0:
    st.write("Conditions are safe.")
elif prediction == 1:
    st.warning("Monitor equipment and inspect safety measures.")
else:
    st.error("Immediate action required. Check machinery and environment.")

st.subheader("Current Inputs")

df = pd.DataFrame({
    "Parameter":["Temperature","Humidity","Gas","Vibration"],
    "Value":[temp,humidity,gas,vibration]
})

st.bar_chart(df.set_index("Parameter"))
import plotly.graph_objects as go

st.subheader("🌍 Global Industrial Monitoring")

fig = go.Figure(go.Scattergeo(
    lon=[77.59, -74.00, 139.69],
    lat=[12.97, 40.71, 35.68],
    mode='markers',
    marker=dict(
        size=[20, 15, 18],
        color=['red', 'orange', 'green']
    ),
    text=[
        'Bangalore Plant',
        'New York Plant',
        'Tokyo Plant'
    ]
))

fig.update_geos(
    projection_type="orthographic",
    showland=True,
    landcolor="rgb(20,20,20)",
    oceancolor="rgb(10,30,60)",
    showocean=True
)

fig.update_layout(
    height=600,
    margin=dict(l=0,r=0,t=0,b=0)
)

st.plotly_chart(fig, use_container_width=True)

