import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Industrial Safety Risk Predictor")

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
