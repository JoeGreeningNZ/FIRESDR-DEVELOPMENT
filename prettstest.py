import pyttsx3
import time

engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-35)

tts = ["SILVERDALE 9 0 1. SILVERDALE 9 0 7", "SILVERDALE 9 0 1.", "SILVERDALE 9 0 7", "SILVERDALE 9 0 1 1", "SILVERDALE 9 0 1. SILVERDALE 9 0 7. SILVERDALE 9 0 1 1", "SILVERDALE 9 0 1. SILVERDALE 9 0 1 1", "SILVERDALE 9 0 7, SILVERDALE 9 0 1 1"]
ttsname = ["17", "1", "7", "11", "1711", "111", "711"]

count = tts.count(tts)

for count in tts:
    engine.say(str(tts[count]))
    engine.save_to_file(tts[count], ttsname[count] + '.wav')
    engine.runAndWait()
    print(ttsname + " " + tts)
    time.sleep(1)




