import streamlit as st
import google.generativeai as genai
from google.api_core import retry
import time

# Configure with error handling
try:
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        st.error("❌ GEMINI_API_KEY not found in Streamlit secrets")
        st.stop()

    genai.configure(api_key=api_key)
    
except Exception as e:
    st.error(f"❌ Configuration failed: {str(e)}")
    st.stop()

MODEL_NAME = "models/gemini-1.5-flash"  # Updated to newer model
MAX_RETRIES = 3
TIMEOUT = 30  # seconds


@retry.Retry(
    initial=1.0,  # Initial delay in seconds
    maximum=10.0,  # Maximum delay
    multiplier=2.0,  # Factor by which delay increases
    deadline=TIMEOUT,  # Total time before giving up
    predicate=retry.if_exception_type(
        Exception
    )  # Retry on all exceptions (be careful with this)
)
def ask_gemini(prompt):
    """Enhanced Gemini query function with retries and error handling"""
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        # More robust response generation
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
            }
        )

        if not response.text:
            raise ValueError("Empty response from Gemini")

        return response.text

    except Exception as e:
        st.warning(f"⚠️ Retrying after error: {str(e)}")
        raise  # Re-raise for retry decorator


def safe_ask_gemini(prompt):
    """Wrapper with additional safety nets"""
    for attempt in range(MAX_RETRIES):
        try:
            return ask_gemini(prompt)
        except Exception as e:
            if attempt == MAX_RETRIES - 1:  # Last attempt failed
                st.error(f"❌ Failed after {MAX_RETRIES} attempts: {str(e)}")
                return None
            time.sleep(1 * (attempt + 1))  # Exponential backoff


if __name__ == "__main__":
    st.title("Gemini API Test")
    test_prompt = st.text_input("Enter test prompt", "Explain Music Blocks in 2 lines.")

    if st.button("Test Gemini"):
        with st.spinner("Asking Gemini..."):
            reply = safe_ask_gemini(test_prompt)
            if reply:
                st.success("✅ Gemini reply:")
                st.write(reply)
                
