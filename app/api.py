from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from JSONParser.json_parser import convert_music_blocks
from retriever.retrieve import retrieve_relevant_chunks
from llm.gemini import ask_gemini
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_INSTRUCTION = """You are Music Blocks Bot, a friendly and playful assistant that helps kids debug their Music Blocks projects. Follow these rules:

1. **Personality**: Be like a patient music teacher who makes learning fun! Use emojis 🎵✨ sometimes to keep it lively.
2. **Language**:
    - Use simple words (max 2 syllables when possible)
    - Short sentences (max 10 words)
3. **Interactivity**:
    - Always ask questions to keep kids engaged
    - Offer choices: "Want to try fixing the drums first or the piano?"
4. **Debugging Help**:
    - Explain problems like stories: "The sleepy trumpet 🎺 isn't waking up because..."
5. **Avoid**:
    - Long paragraphs
    - Technical words without explaining
    - Negative language (say "Let's try again!" not "You're wrong")
6. **When stuck**:
    - Offer to "ask a grownup" if too hard
    - Suggest taking a music break and coming back
"""

@app.post("/analyze")
async def analyze(request: Request):
    try:
        data = await request.json()
        raw_json_code = data.get("code", "")
        user_prompt = data.get("prompt", "")
        chat_history = data.get("history", [])
        prompt_count = data.get("prompt_count", 1)

        if not raw_json_code:
            return JSONResponse(status_code=400, content={"error": "Missing code"})

        try:
            json_data = raw_json_code if isinstance(raw_json_code, dict) else json.loads(raw_json_code)
            converted_code = "\n".join(convert_music_blocks(json_data))
        except json.JSONDecodeError as e:
            return JSONResponse(status_code=400, content={"error": f"Invalid JSON: {str(e)}"})

        context_chunks = retrieve_relevant_chunks(converted_code + user_prompt)

        if not user_prompt:
            prompt = (
                SYSTEM_INSTRUCTION + "\n\n"
                + "You are being given a Music Blocks project code. Your task is to analyze this code and try to understand what the student is trying to build — is it a melody, a rhythm, a loop-based song, an instrument experiment, a math-based music pattern, etc.?\n\n"
                + "Here is the full Music Blocks project code:\n"
                + converted_code + "\n\n"
                + "Helpful parts from documentation or examples:\n"
                + "\n".join(context_chunks) + "\n\n"
                + "Now make your best guess: Start your message like this —\n"
                + "\"It appears to me that your project is about...\" 🎶\n"
                + "Then ask: \"Did I get that right? What else do you want to tell me about your project before we begin debugging?\"\n\n"
                + "Keep your answer lively, musical, and kid-friendly. Use emojis where helpful. Keep sentences short and clear."
            )
        else:
            if prompt_count < 2:
                tone = (
                    "You should keep the tone curious and keep asking questions to understand what the student wants to do. "
                    "Keep things fun, ask what they’re trying to build, and make them feel excited to share more! 🎵"
                )
            else:
                tone = (
                    "Now it’s time to help more directly. Suggest changes to fix bugs, improve the music, or try new things. "
                    "Be confident, proactive, and guide them clearly through small changes. Offer direct help instead of just asking questions. 🎯"
                )

            history_text = ""
            for turn in chat_history:
                role = "🎧 You" if turn["role"] == "user" else "🎹 Music Blocks Bot"
                history_text += f"{role}: {turn['content']}\n"

            prompt = (
                SYSTEM_INSTRUCTION + "\n\n"
                + tone + "\n\n"
                + "Here is the full Music Blocks project code:\n"
                + converted_code + "\n\n"
                + "Here are helpful parts from documentation or examples:\n"
                + "\n".join(context_chunks) + "\n\n"
                + "Conversation history so far:\n"
                + history_text
                + f"🎧 You: {user_prompt}\n🎹 Music Bot:"
            )

        gemini_response = ask_gemini(prompt)

        return JSONResponse(content={
            "response": gemini_response
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Internal server error: {str(e)}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)