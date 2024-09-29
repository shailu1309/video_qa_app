from pytube import YouTube
import speech_recognition as sr
import os

def download_video(video_url):
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    audio_file = video.download(filename='audio.mp4')
    return audio_file

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    # Clean up the audio file after processing
    os.remove(audio_file)
    return text
