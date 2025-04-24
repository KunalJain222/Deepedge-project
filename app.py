import os
os.makedirs("streamlit_app", exist_ok=True)

#streamlit_app/app.py
import streamlit as st
import requests

BACKEND_URL = "http://localhost:5000/generate"

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def get_response(query):
    try:
        response = requests.post(
            BACKEND_URL,
            json={'query': query},
            headers={'Content-Type': 'application/json'}
        )
        return response.json()['response']
    except Exception as e:
        return f"Error: {str(e)}"

st.title("RAG Chatbot")

user_input = st.text_input("Ask a question:")
if user_input:
    st.session_state.chat_history.append(("You", user_input))
    
    response = get_response(user_input)
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
    st.write(f"{sender}: {message}")