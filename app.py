# app.py
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from helpers import summarize_df, ask_model

load_dotenv() # loads .env

st.set_page_config(page_title="AI Data Support Agent", layout="wide")
st.title("AI Support Agent for Data Analysis (Excel)")

st.markdown(
 "Upload an Excel file (.xlsx or .xls). The app will summarize the data and let you ask analysis questions."
)

uploaded = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

if uploaded:
 # pandas can read file-like objects from Streamlit uploader
 try:
  df = pd.read_excel(uploaded)
 except Exception as e:
  st.error(f"Failed to read Excel file: {e}")
  st.stop()

 st.subheader("Preview")
 st.write(df.head())

 st.subheader("Dataset Summary")
 st.json(summarize_df(df))

 question = st.text_input("Ask a question about this data (e.g., 'Which columns predict sales?')")

 if st.button("Ask AI") and question.strip():
  api_key = os.getenv("GEMINI_API_KEY")
  with st.spinner("Querying Gemini..."):
   answer = ask_model(df, question, api_key)
  st.subheader("AI Answer")
  st.write(answer)