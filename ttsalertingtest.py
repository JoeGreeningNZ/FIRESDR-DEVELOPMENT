import pyttsx3
from subprocess import call

active = True

engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-35)

tts = "Silverdale 9 0 1. Silverdale  90 7.  Minor Incident. Car Leaking Fuel. Yellow Watch. Respond. Second Out Crew Respond. 20 Jack Hawkin Lane. Cross Street With Hibiscus Coast Highway"

while active:
    call(["aplay", "/home/pi/FIRESDR/tone.wav"])
    engine.say(tts)
    engine.save_to_file(tts, 'tts.wav')
    engine.runAndWait()
    print("TTS")
    active = False




