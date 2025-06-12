import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from retriever.retrieve import retrieve_relevant_chunks
from llm.gemini import ask_gemini

st.set_page_config(page_title="🎵 Music Blocks Debugger")

st.title("Music Blocks Debugger 💬")

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "project_code" not in st.session_state:
    st.session_state.project_code = ""

with st.expander("🧩 Step 1: Enter your Music Blocks Project Code", expanded=not st.session_state.project_code):
    code = st.text_area("Paste your Music Blocks Project Code here:", height=300)
    if st.button("Initialize Project Code"):
        if code.strip():
            st.session_state.project_code = code.strip()
            st.success("Project code saved! You can now ask questions below.")
        else:
            st.warning("Please enter a valid Music Blocks project code.")

if st.session_state.project_code:
    st.subheader("💬 Ask Questions About Your Project")

    user_input = st.chat_input("Ask something about the Music Blocks project...")

    if user_input:
        with st.spinner("Gemini is thinking..."):
            try:
                conversation = f"Here is a Music Blocks project code:\n{st.session_state.project_code}\n\n"
                for turn in st.session_state.chat_history:
                    role = "User" if turn["role"] == "user" else "Gemini"
                    conversation += f"{role}: {turn['content']}\n"
                conversation += f"User: {user_input}\nGemini:"

                context_chunks = retrieve_relevant_chunks(st.session_state.project_code + user_input)
                final_prompt = "\n".join(context_chunks) + "\n\n" + conversation

                gemini_reply = ask_gemini(final_prompt)

                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.chat_history.append({"role": "gemini", "content": gemini_reply})

            except Exception as e:
                st.error(f"Gemini API error: {str(e)}")

    for turn in st.session_state.chat_history:
        with st.chat_message("user" if turn["role"] == "user" else "assistant"):
            st.markdown(turn["content"])

    scroll_script = """
    <script>
        setTimeout(function() {
            var chatAnchor = document.getElementById("bottom-anchor");
            if (chatAnchor) {
                chatAnchor.scrollIntoView({ behavior: "smooth" });
            }
        }, 100);  // Delay scrolling slightly to ensure DOM is ready
    </script>
    <div id="bottom-anchor"></div>
    """
    st.components.v1.html(scroll_script, height=0)

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.success("Chat history cleared.")
else:
    st.info("Please enter your Music Blocks project code above to begin debugging.")
