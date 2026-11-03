import streamlit as st
st.title("AI Streamlit App")
st.write("AI enabled Web Application  using Streamlit Cloud Community
Cloud.")
name = st.text_input("Enter your name")
if st.button("Submit"):
st.success(f"Hello, {name}! Your application is running successfully.")