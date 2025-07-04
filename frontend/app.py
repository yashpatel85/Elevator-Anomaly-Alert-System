import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title = 'Elevator Anomaly Alert', page_icon = "🚨")

st.title('Elevator Anomaly Detection System')
st.markdown('Enter sensor readings below to check for anomalies')

feature_names = [
    'vibration_mean', 'vibration_std', 'vibration_max', 'vibration_min',
    'humidity_mean', 'humidity_std', 'humidity_max', 'humidity_min',
    'revolution_mean', 'revolution_std', 'revolution_max', 'revolution_min'
]

data = {}
with st.form('input_form'):
    for name in feature_names:
        data[name] = st.number_input(name.replace("_"," ").title(), format = '%.4f')
    submitted = st.form_submit_button('Submit for Prediction')

if submitted:
    try:
        res = requests.post("http://127.0.0.1:5000/predict", json = data)
        if res.status_code == 200:
            result = res.json()
            st.success("✅ Prediction Received:")
            st.metric("Anomaly Score", f"{result['anomaly_score']:.4f}")
            st.metric("Is Anomaly", "⚠️ YES" if result['is_anomaly'] else '✅ NO')

            if result["is_anomaly"]:
                st.error("🚨 ***Anomaly Detected!!! Immediate Attention Required!***", icon = '🚨')
                st.balloons
            else:
                print("✅ Everything looks normal")
        else:
            st.error(f"❌ Error: {res.json().get('error', 'Something went wrong.')}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to Flask API. Make sure it's running at http://127.0.0.1:5000")


st.markdown("---")
st.subheader("📊 Anomaly Score Logs")

log_file = "logs/predictions.csv"

try:
    df = pd.read_csv(log_file, parse_dates = ['timestamp'])

    st.markdown("### 📈 Anomaly Score Over Time")
    st.line_chart(data = df.set_index('timestamp')['anomaly_score'])

    st.markdown("### 🧮 Score Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['anomaly_score'], bins = 30, kde = True, ax = ax, color = 'skyblue')
    ax.axvline(x = -0.15, color = 'red', linestyle = '--', label = 'Threshold (-0.15)')
    ax.set_xlabel('Anomaly Score')
    ax.legend()
    st.pyplot(fig)

    st.markdown('### ⚠️ Anomaly Summary')
    count = df['is_anomaly'].sum()
    st.metric("Detected Anomalies", count)

except FileNotFoundError:
    st.warning("No logs found yet. Submit some predictions first.")