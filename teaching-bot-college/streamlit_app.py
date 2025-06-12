import streamlit as st
from backend.content_generator import generate_content
from backend.image_fetcher import fetch_diagram_image
from backend.voice_generator import text_to_speech
from backend.supabase_client import save_lesson

st.title(" 🧠 NeoTutor")
topic = st.text_input("Enter the topic you want to learn")
if st.button("📘 Generate Lesson"):
    with st.spinner("📄 Generating..."):
        content = generate_content(topic)
        img_url = fetch_diagram_image(topic)
        audio_path = text_to_speech(content)
        save_lesson(topic, content)
        st.subheader("📝 Lesson Notes")
        st.markdown(content)
        st.subheader("🖼️ Diagram")
        st.image(img_url)
        st.subheader("🔊 Audio Explanation")
        with open(audio_path, 'rb') as audio_file:
            st.audio(audio_file.read(), format='audio/mp3')
