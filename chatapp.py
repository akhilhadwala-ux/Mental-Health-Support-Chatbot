import os
import re
from google import genai
import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

load_dotenv()

# =========================
# API KEY
# =========================
api_key = os.getenv("gemini_key")

if not api_key:
    st.error("API key not found. Check your .env file")
    st.stop()

# =========================
# CLIENT INIT
# =========================
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

client = st.session_state.client

st.title("Mental Health Support Chatbot")

# =========================
# SYSTEM PROMPT
# =========================
system_prompt = """
You are a compassionate, supportive, and non-judgmental mental health support assistant. 
Your role is to provide emotional support, coping strategies, and general guidance,
while respecting your limitations as an AI (not a licensed therapist or medical professional). 
Use empathetic, validating language and respond concisely, typically in 1–3 sentences, 
adjusting length when needed to provide meaningful support. Ask gentle, open-ended questions when appropriate. 
Do not diagnose conditions or provide medical treatment.
If the user expresses distress related to self-harm or suicide,
respond with empathy and encourage them to seek help from trusted people, local emergency services, or crisis helplines.
"""

# =========================
# CHAT SESSION
# =========================
if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash-lite",
        config=genai.types.GenerateContentConfig(
            system_instruction=system_prompt,
        )
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# DISPLAY CHAT HISTORY
# =========================
for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")

# =========================
# INPUT VALIDATION MODEL
# =========================
class InputFormat(BaseModel):

    input: str = Field(description="User message")

    @field_validator("input")
    @classmethod
    def validate_input(cls, value):

        value = value.strip()

        # Empty check
        if not value:
            raise ValueError("Donot provide empty spaces as Input. Please provide a valid input")

        # Minimum word check
        if len(value.split()) < 5:
            raise ValueError("Input must contain at least 5 words")

        # Numeric-only check
        if re.fullmatch(r'[\d\s]+', value):
            raise ValueError("Numeric-only input is not allowed")

        return value


# =========================
# OUTPUT VALIDATION MODEL
# =========================
class OutputFormat(BaseModel):

    output: str = Field(description="Bot response")

    @field_validator("output")
    @classmethod
    def validate_output(cls, value):

        value = value.strip()

        # Empty response check
        if not value:
            raise ValueError("Model returned an empty response")

        # Very short response check
        if len(value.split()) < 3:
            raise ValueError("Response too short")

        # Prevent extremely long outputs
        if len(value.split()) > 120:
            raise ValueError("Response too long")
# =========================
# USER INPUT
# =========================
user_input = st.chat_input("Type your message here...")

if user_input:

    try:
        # Validate input
        validated_input = InputFormat(input=user_input)

        clean_input = validated_input.input

        # Send to Gemini
        chat = st.session_state.chat_session
        response = chat.send_message(clean_input)

        # Raw model output
        raw_reply = response.text

        # Validate output
        validated_output = OutputFormat(output=raw_reply)

        bot_reply = validated_output.output

        # Save bot message
        st.session_state.messages.append(
            ("bot", bot_reply)
        )

        st.rerun()

    except Exception as e:
        st.error(str(e))