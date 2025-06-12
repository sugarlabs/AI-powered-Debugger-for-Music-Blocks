import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GEMINI_API_KEY"]
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in Streamlit secrets")

genai.configure(api_key=api_key)

MODEL_NAME = "models/gemini-2.0-flash"

def ask_gemini(prompt):
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    reply = ask_gemini("Explain Music Blocks in 2 lines.")
    print("✅ Gemini reply:\n", reply)
