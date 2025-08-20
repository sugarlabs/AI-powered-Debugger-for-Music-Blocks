import google.generativeai as genai
from google.api_core import retry
import time
import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
    api_key = st.secrets.get("GEMINI_API_KEY")
except (ImportError, AttributeError):
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in either Streamlit secrets or environment variables")

genai.configure(api_key=api_key)

MODEL_NAME = "models/gemini-1.5-flash"
MAX_RETRIES = 3
TIMEOUT = 30

@retry.Retry(
    initial=1.0,
    maximum=10.0,
    multiplier=2.0,
    deadline=TIMEOUT,
    predicate=retry.if_exception_type(Exception),
)
def ask_gemini(prompt: str) -> str:
    """Send prompt to Gemini and return the response text."""
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 2000,
            },
            safety_settings={
                "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
                "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
                "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
                "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
            },
        )

        if hasattr(response, "text") and response.text:
            return response.text

        try:
            return response.candidates[0].content.parts[0].text
        except Exception:
            st.warning("Could not access `.text`, trying candidates[0].content.parts[0].text")
            st.code(str(response))
            raise ValueError("Gemini response format is unexpected.")

    except Exception as e:
        st.warning(f"Retrying due to error: {str(e)}")
        raise

def safe_ask_gemini(prompt: str) -> str | None:
    """Wrapper to retry Gemini call up to MAX_RETRIES."""
    for attempt in range(MAX_RETRIES):
        try:
            return ask_gemini(prompt)
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                st.error(f"Gemini failed after {MAX_RETRIES} attempts: {e}")
                return None
            time.sleep(1 * (attempt + 1))
            return None
    return None

if __name__ == "__main__":
    st.title("Gemini API Test")
    prompt = st.text_input("Enter prompt", "Explain Music Blocks in 2 lines.")

    if st.button("Ask Gemini"):
        with st.spinner("Thinking..."):
            reply = safe_ask_gemini(prompt)
            if reply:
                st.success("Gemini replied:")
                st.write(reply)
