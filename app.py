import streamlit as st
import pandas as pd

st.title("Trader Behavior Dashboard")

df = pd.read_csv("final_data.csv")
st.write("### Data Preview")
st.dataframe(df.head())

st.write("### PnL by Sentiment")
st.bar_chart(df.groupby('Classification')['closedPnL'].mean())

st.write("### Trade Size Distribution")
st.bar_chart(df.groupby('Classification')['size'].mean())