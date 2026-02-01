import streamlit as st
import requests

st.title("AI Chatbot using LLM")

user_input = st.text_input("You:")

if user_input:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    )

    if response.status_code == 200:
        st.write("Bot:", response.json()["reply"])
    else:
        st.error("Backend error. Is FastAPI running?")
