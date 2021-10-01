import gtts
from playsound import playsound
import os

TEXT = input("What do you want me to say: ")

tts = gtts.gTTS(f"{TEXT}", lang="en")

# save the audio file
tts.save(f"{TEXT}.mp3")

# play the audio file
playsound(f"{TEXT}.mp3")

os.remove(f"{TEXT}.mp3")