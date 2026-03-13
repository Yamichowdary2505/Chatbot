import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from prompts import get_tutor_prompt, get_code_prompt, get_interview_prompt, get_summary_prompt

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("💬 Chatbot")

mode = st.selectbox("Select Mode", ["Tutor", "Code Assistant", "Interview Coach", "Summarizer"])

if "chat" not in st.session_state or st.session_state.get("current_mode") != mode:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []
    st.session_state.current_mode = mode

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask question to Chatbot:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    if mode == "Tutor":
        prompt = get_tutor_prompt(user_input)
    elif mode == "Code Assistant":
        prompt = get_code_prompt(user_input)
    elif mode == "Interview Coach":
        prompt = get_interview_prompt(user_input)
    elif mode == "Summarizer":
        prompt = get_summary_prompt(user_input)

    response = st.session_state.chat.send_message(prompt)
    reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
