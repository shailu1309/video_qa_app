# app.py

import streamlit as st
from audio_processing import download_video, transcribe_audio
from utils import ask_question

# Streamlit app header
st.title("Video Q&A Application")

# Input fields for video URL and question
video_url = st.text_input("Enter the YouTube Video URL:")
question = st.text_input("Enter your question about the video:")

if st.button("Ask"):
    if video_url and question:
        with st.spinner("Processing..."):
            try:
                # Download video and transcribe audio
                audio_file = download_video(video_url)
                transcript = transcribe_audio(audio_file)

                # Ask the question
                answer = ask_question(transcript, question)
                
                # Display the answer
                st.success("Answer: " + answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both a video URL and a question.")
