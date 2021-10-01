import gtts
from playsound import playsound
import os

TEXT = input("Qué quieres que te diga: ")

tts = gtts.gTTS(f"{TEXT}", lang="es")

# save the audio file
tts.save(f"{TEXT}.mp3")

# play the audio file
playsound(f"{TEXT}.mp3")

os.remove(f"{TEXT}.mp3")