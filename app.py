from deep_translator import GoogleTranslator
from gtts import gTTS
import streamlit as st
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
st.markdown("""
<div style='text-align: center;'>
    <p style='font-size:18px; color: white;'>❤ Not just AI — it’s <b>Kripa’s heart</b> in every word ✨</p>
    <img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXZoNmx6ZHA1MzRoanI1b2w4ODR5czJ3Z3M3N3N4bXRhMjNpM29sZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/4dJRDQSbjFigYkbEe0/giphy.gif' width='50'>
</div>
""", unsafe_allow_html=True)
#st.write("Not Just AI -- it's Kripa's heart in every word ")


# ✅ These inputs MUST come first:
text_input = st.text_area("💬 Enter text to translate")
src_lang = st.text_input("🔤 Source Language (e.g., 'en')", value='en')
dest_lang = st.text_input("🌏 Target Language (e.g., 'fr')", value='fr')

# ✅ Then your Translate button:
if st.button("✨ Translate Now ✨"):
    if text_input:
        try:
            translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(text_input)
            st.success(f"🌟 Translated Text: {translated_text}")

            # Text-to-Speech
            tts = gTTS(translated_text, lang=dest_lang)
            tts.save("translated.mp3")

            # Listen & Download
            with open("translated.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")

                b64 = base64.b64encode(audio_bytes).decode()
                href = f'<a href="data:audio/mp3;base64,{b64}" download="translated.mp3">💾 Download Translated Audio</a>'
                st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠ Error: {e}")
    else:
        st.error("⚠ Please enter text to translate!")

st.markdown("""
---
<p style='text-align: center; color: white;'>
Made with ❤ by <b>Kripa Sharma</b> 
</p>
""", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Thank you 🫶🏻</h4>", unsafe_allow_html=True)
