import random
import streamlit as st

# Fake speech-to-text simulation
def fake_recording_ui():
    with st.spinner("🎙 Listening... (simulated recording)"):
        st.markdown("#### 🔴 Recording in progress...")
        st.markdown("_(Say something clearly...)_")

# Function to simulate Gemini answering a random sentence from context
def gemini_fake_speech_answer(context):
    sentences = [s.strip() for s in context.strip().split('.') if s.strip()]
    if not sentences:
        return "No valid sentence found in context."
    return random.choice(sentences) + "."
