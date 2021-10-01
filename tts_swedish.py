import gtts
from playsound import playsound
import os

TEXT = input("Vad vill du att jag ska säga: ")

tts = gtts.gTTS(f"{TEXT}", lang="sv")

# save the audio file
tts.save(f"{TEXT}.mp3")

# play the audio file
playsound(f"{TEXT}.mp3")

os.remove(f"{TEXT}.mp3")