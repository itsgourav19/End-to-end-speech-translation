from moviepy.editor import VideoFileClip
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Path to the video file
video_path ="RAW\RIISE 2022 final video.mp4"
# Load the video file
video = VideoFileClip(video_path)

# Extract audio from the video
audio = video.audio

# Save the audio as a temporary file
audio_temp_path = "temp_audio.wav"
audio.write_audiofile(audio_temp_path)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile(audio_temp_path) as source:
    audio_data = recognizer.record(source)

# Perform speech recognition
text = recognizer.recognize_google(audio_data)

# Function to translate text from English to Hindi
def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='hi')
    return translated_text.text

# Translate the recognized text
translated_text = translate_text(text)

# Output the translated text
print("Translated Text (English to Hindi):", translated_text)

# Convert translated text to Hindi speech
tts = gTTS(text=translated_text, lang='hi')
tts.save("translated_speech_hindi.mp3")

# Clean up - remove temporary audio file
os.remove(audio_temp_path)