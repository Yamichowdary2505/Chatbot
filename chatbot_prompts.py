from google import genai
from dotenv import load_dotenv
import os
from prompts import get_tutor_prompt, get_code_prompt, get_interview_prompt, get_summary_prompt

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Select mode:")
print("1 - Tutor")
print("2 - Code Assistant")
print("3 - Interview Coach")
print("4 - Summarizer")

mode = input("Enter mode number: ")

chat = client.chats.create(model="gemini-2.5-flash")

while True:
    user_input = input("Ask question to Chatbot: ")
    if user_input.lower() == "exit":
        break

    if mode == "1":
        prompt = get_tutor_prompt(user_input)
    elif mode == "2":
        prompt = get_code_prompt(user_input)
    elif mode == "3":
        prompt = get_interview_prompt(user_input)
    elif mode == "4":
        prompt = get_summary_prompt(user_input)
    else:
        prompt = user_input

    response = chat.send_message(prompt)
    print("ChatBot: ", response.text)