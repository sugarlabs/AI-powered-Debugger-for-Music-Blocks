import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from JSONParser.json_parser import convert_music_blocks
import json
import streamlit as st
from retriever.retrieve import retrieve_relevant_chunks
from llm.gemini import ask_gemini
from datetime import datetime

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
    if st.button("🚀 Launch My Music Blocks Project!"):
        if code.strip():
            try:
                try:
                    json_data = json.loads(code.strip())
                    converted_text = "\n".join(convert_music_blocks(json_data))
                    st.session_state.project_code = converted_text
                except json.JSONDecodeError as e:
                    st.error(f"Invalid JSON format: {str(e)}")
                    st.stop()

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
            except Exception as e:
                st.error(f"Error processing project code: {str(e)}")
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

                if st.session_state.user_prompt_count < 2:
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

    def generate_chat_export():
        export_content = "Music Blocks Debugger Chat Export\n"
        export_content += f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        export_content += "Project Code:\n"
        export_content += st.session_state.project_code + "\n\n"
        export_content += "Chat History:\n\n"

        for turn in st.session_state.chat_history:
            role = "You" if turn["role"] == "user" else "Music Blocks Bot"
            export_content += f"{role}:\n{turn['content']}\n\n"

        return export_content

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

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.chat_history:
            st.download_button(
                "💾 Export Chat",
                data=generate_chat_export(),
                file_name=f"music_blocks_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                help="Download the full chat history as a text file"
            )
        else:
            st.button("💾 Export Chat", disabled=True, help="No chat history to export yet")

    with col2:
        if st.button("🗑️ Clear Chat", help="Clear all chat messages"):
            st.session_state.chat_history = []
            st.success("Chat history cleared!")
