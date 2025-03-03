import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset (Example: Global Temperature Data)
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv"
    df = pd.read_csv(url)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Streamlit App
st.title("🌍 Global Warming
