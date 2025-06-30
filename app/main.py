import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from retriever.retrieve import retrieve_relevant_chunks
from llm.gemini import ask_gemini

st.set_page_config(page_title="🎵 Music Blocks Debugger")

st.title("🎵 Music Blocks Debugger")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "project_code" not in st.session_state:
    st.session_state.project_code = ""
if "user_prompt_count" not in st.session_state:
    st.session_state.user_prompt_count = 0

SYSTEM_INSTRUCTION = (
     """You are Music Blocks Bot, a friendly and playful assistant that helps kids debug their Music Blocks projects. Follow these rules:

        1. **Personality**: Be like a patient music teacher who makes learning fun! Use emojis 🎵✨ sometimes to keep it lively.

        2. **Language**: 
            - Use simple words (max 2 syllables when possible)
            - Short sentences (max 10 words)
            - Examples: "Oh no! Your drums are too quiet 🥁 Let's turn them up!" or "Wow! That's a cool melody! 🎶"
   
        3. **Interactivity**:
            - Always ask questions to keep kids engaged
            - Offer choices: "Want to try fixing the drums first or the piano?" 
            - Give high-fives for good work: "You fixed it! 🙌"

        4. **Debugging Help**:
            - Explain problems like stories: "The sleepy trumpet 🎺 isn't waking up because..."
            - Show don't tell - use simple comparisons: "Your loop is like a hamster wheel that never stops!"

        5. **Avoid**:
            - Long paragraphs
            - Technical words without explaining
            - Negative language (say "Let's try again!" not "You're wrong")

        6. **When stuck**:
            - Offer to "ask a grownup" if too hard
            - Suggest taking a music break and coming back

        First respond to the user by introducing yourself excitedly and asking about their Music Blocks project in a fun way! 🎼"""
)

with st.expander("🎒 Drop Your Music Blocks Project Here!", expanded=not st.session_state.project_code):
    code = st.text_area("🎼 Paste your magical music code below ✨", height=300)
    if st.button("🚀 Launch My Music Project!"):
        if code.strip():
            st.session_state.project_code = code.strip()
            st.success("Project code saved !!")

            with st.spinner("🎼 The Debugger is tuning its ears..."):
                try:
                    context_chunks = retrieve_relevant_chunks(st.session_state.project_code)

                    intro_prompt = (
                            SYSTEM_INSTRUCTION + "\n\n"
                            + "You are being given a Music Blocks project code. Your task is to analyze this code and try to understand what the student is trying to build — is it a melody, a rhythm, a loop-based song, an instrument experiment, a math-based music pattern, etc.?\n\n"
                            + "Here is the full Music Blocks project code:\n"
                            + st.session_state.project_code + "\n\n"
                            + "Helpful parts from documentation or examples:\n"
                            + "\n".join(context_chunks) + "\n\n"
                            + "Now make your best guess: Start your message like this —\n"
                            + "\"It appears to me that your project is about...\" 🎶\n"
                            + "Then ask: \"Did I get that right? What else do you want to tell me about your project before we begin debugging?\"\n\n"
                            + "Keep your answer lively, musical, and kid-friendly. Use emojis where helpful. Keep sentences short and clear."
                    )

                    gemini_intro_reply = ask_gemini(intro_prompt)

                    st.session_state.chat_history.append({
                        "role": "gemini",
                        "content": gemini_intro_reply
                    })

                except Exception as e:
                    st.error(f"Gemini API error during intro message: {str(e)}")
        else:
            st.warning("Please enter a valid Music Blocks project code.")

if st.session_state.project_code:
    st.subheader("🎼 Curious Notes? Let’s Debug Together!")

    user_input = st.chat_input("🎹 Got a music mystery to solve?")

    if user_input:
        st.session_state.user_prompt_count += 1
        with st.spinner("🎼 The Debugger is tuning its ears..."):
            try:
                context_chunks = retrieve_relevant_chunks(st.session_state.project_code + user_input)

                conversation = ""
                for turn in st.session_state.chat_history:
                    role = "🎧 You" if turn["role"] == "user" else "🎹 Music Blocks Bot"
                    conversation += f"{role}: {turn['content']}\n"

                mode_instruction = ""

                if st.session_state.user_prompt_count < 4:
                    mode_instruction = (
                        "You should keep the tone curious and keep asking questions to understand what the student wants to do. "
                        "Keep things fun, ask what they’re trying to build, and make them feel excited to share more! 🎵"
                    )
                else:
                    mode_instruction = (
                        "Now it’s time to help more directly. Suggest changes to fix bugs, improve the music, or try new things. "
                        "Be confident, proactive, and guide them clearly through small changes. Offer direct help instead of just asking questions. 🎯"
                    )

                final_prompt = (
                        SYSTEM_INSTRUCTION + "\n\n"
                        + mode_instruction + "\n\n"
                        + "Here is the full Music Blocks project code:\n"
                        + st.session_state.project_code + "\n\n"
                        + "Here are helpful parts from documentation or examples:\n"
                        + "\n".join(context_chunks) + "\n\n"
                        + "Conversation history so far:\n"
                        + conversation
                        + f"🎧 You: {user_input}\n🎹 Music Bot:"
                )

                gemini_reply = ask_gemini(final_prompt)

                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.chat_history.append({"role": "music_blocks_bot", "content": gemini_reply})

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
        }, 100);
    </script>
    <div id="bottom-anchor"></div>
    """
    st.components.v1.html(scroll_script, height=0)

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.success("Chat history cleared.")
    else:
        st.info("Please enter your Music Blocks project code above to begin debugging.")
