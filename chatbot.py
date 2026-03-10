import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

while True:
    user_input = input("Ask question to Chatbot: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("ChatBot: ", response.text)