import streamlit as st
from googletrans import Translator
from gtts import gTTS
import base64

st.set_page_config(page_title="🌸 AI Translator", page_icon="🌸", layout="centered")
st.markdown("""
    <style>
    h1 {
        font-size: 60px;
        font-family: 'Comic Sans MS', cursive;
        color: #fff;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Custom CSS for Anime Vibe
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #ff5e78;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0px 0px 15px #ff99aa;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff99aa;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Anime GIF at the top
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2tlcDR4ZjYzdjJhYnRseGgyNHp3eDVmaGQwc21jczd2YjY2MHB5NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/T8P5JC0Le4z5eEI6Ub/giphy.gif' width='250'>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1>🪄AI Language Translator🪄</h1>", unsafe_allow_html=True)
st.write("✨ Translate with cuteness overload! ✨")

translator = Translator()

text_input = st.text_area("💬 Enter text to translate")
src_lang = st.text_input("🔤 Source Language (e.g., 'en' for English)", value='en')
dest_lang = st.text_input("🌏 Target Language (e.g., 'ja' for Japanese)", value='ja')

if st.button("✨ Translate Now ✨"):
    if text_input:
        translated = translator.translate(text_input, src=src_lang, dest=dest_lang)
        st.success(f"🌟 Translated Text: {translated.text}")

        # Text to Speech
        tts = gTTS(translated.text, lang=dest_lang)
        tts.save("anime_translated.mp3")
        audio_file = open("anime_translated.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        # Download Link
        b64 = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{b64}" download="anime_translated.mp3">💾 Download Audio</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.error("⚠ Please enter text to translate!")