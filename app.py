import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import datetime
import re
from core import process_data

st.set_page_config(page_title="ADS-B Spoof Detection", layout="wide")

# ========================
# USER ENTRY
# ========================
st.title("Enter Details")

name = st.text_input("Name", max_chars=50)
email = st.text_input("Email", max_chars=100)

def valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e)

if st.button("Enter"):
    if name and email and valid_email(email):
        st.session_state["user"] = name
        st.session_state["entered"] = True
    else:
        st.warning("Enter valid details")

if "entered" not in st.session_state:
    st.stop()

# ========================
# TRACK USER
# ========================
with open("visitors.txt", "a") as f:
    f.write(f"{name} - {datetime.datetime.now()}\n")

# ========================
# MAIN APP
# ========================
st.title("ADS-B Spoof Detection System")

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# INPUT
lat = st.number_input("Latitude", -90.0, 90.0, 20.0)
lon = st.number_input("Longitude", -180.0, 180.0, 75.0)
velocity = st.number_input("Velocity", 0.0, 2000.0, 300.0)

if st.button("Predict"):
    sample = {f: 0 for f in features}
    sample.update({"lat": lat, "lon": lon, "velocity": velocity})
    df_input = pd.DataFrame([sample])
    
    pred = model.predict(df_input)[0]
    st.success("Normal" if pred == 0 else "Spoofed")

# ========================
# DATA + MAP
# ========================
try:
    df = pd.read_csv("data/adsb_data.csv").sample(50000)
except:
    st.error("Data error")
    st.stop()

df = process_data(df)

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    color="label",
    zoom=3
)

fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig, key="map1")

st.markdown("---")
st.write("Developed by Zuha Jagirdar")