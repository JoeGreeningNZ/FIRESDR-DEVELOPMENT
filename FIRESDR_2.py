#FIRESDR Smart Paging - Created By Joe Greening - F§P - Version 2

# Color Mapping
# Red - Turnout - \033[1;31;40m
# Yellow - Standby - \033[1;33;40m
# Green - Message - \033[1;32;40m
# Cyan - System - \033[1;36;40m
# Magenta - Error - \033[1;35;40m
# White - Shell - \033[1;37;40m

import os
from subprocess import call
import pyttsx3
import time
import holidays
from datetime import datetime
from chump import Application

active = True
tts = ""
msg = ""

typeabbr = {'MIN': 'MINOR INCIDENT',
            'STRU': 'STRUCTURE INCIDENT',
            'MED': 'MEDICAL',
            'MEDFR': 'MEDICAL FIRST RESPONSE',
            'RESC': 'RESCUE',
            'VEG': 'VEGETATION FIRE',
            'NAT1': 'NATURAL EVENT - PRIORITY 1',
            'NAT2': 'NATURAL EVENT - PRIORITY 2',
            'HAZ': 'HAZARDOUS SUBSTANCE INCIDENT',
            'HAZGAS': 'HAZARDOUS GAS INCIDENT',
            }

roadabbr = {' RD': ' ROAD ',
            ' AV': ' AVENUE ',
            ' PL': ' PLACE ',
            ' CL': ' CLOSE ',
            ' CT': ' COURT ',
            ' CR': ' CRESENT ',
            ' DR': ' DRIVE ',
            ' EXP': ' EXPRESSWAY ',
            ' HWY': ' HIGHWAY ',
            ' GR': ' GROVE ',
            ' HTS': ' HEIGHTS ',
            ' LN': ' LANE ',
            ' ST': ' STREET ',
            ' WAY': ' WAY ',
            ' TCE': ' TERRACE ',
            ' MWY': ' MOTORWAY ',
            ' PDE': ' PARADE ',
            ' CNR': ' CORNER ',
            ' ESP': ' ESPLANADE ',
            }

#FIRESDR Smart Paging (Application)
app = Application('a37fksysrfhmnuaczz58qaxqj4qb4o')
#FIRESDR Smart Paging Members (Delivery Group)
user = app.get_user('g89nanv98y2znbrt2xn2i8zpitv4ay')

#Initialise TTS engine
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-35)

#Initialise Variables for Yellow Watch.
yw_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
yw_start = '07:05:00'
yw_end = '17:25:00'
yw_holidays = []
prev_check = ""
yw_active = False

#Sort Holidays for Yellow Watch
for holiday in holidays.NZ(years=[2022]).items():
    if ((holiday[0]).weekday()) <= 5:
        yw_holidays.append(holiday[0].strftime('%d-%m-%y'))

def yw_check():
    currday = datetime.today().strftime('%A') # Monday
    currdate = datetime.today().strftime('%D-%M-%Y') # 00/00/0000
    currtime = datetime.now().strftime("%H:%M:%S") # 00:00:00   
    if (currdate in yw_holidays):
        return "\033[1;31;40mOff Duty - Public Holiday"
    elif (currday not in yw_days):
        return "\033[1;31;40mOff Duty - Weekend"
    elif (yw_start <= currtime <= yw_end):
        return "\033[1;32;40mOn Duty"
    else:
        return "\033[1;31;40mOff Duty - Outside YW Hours"



#Define Turnout Actions and Proccesses for Smart Paging through Pushover and External Speakers.
def turnout(stage):
    if stage != 0:
        if stage == 1:
            call(["aplay","/home/pi/FIRESDR/tone.wav"])
        if stage == 2:
            call(["aplay", "/home/pi/FIRESDR/tone.wav"])
            call(["aplay", "/home/pi/FIRESDR/tone.wav"])
        if stage == 3:
            call(["aplay", "/home/pi/FIRESDR/tone.wav"])
            call(["aplay", "/home/pi/FIRESDR/tone.wav"])
            call(["aplay", "/home/pi/FIRESDR/tone.wav"])
    engine.say(tts)
    engine.runAndWait()
    message = user.send_message(msg) #*************************** Comment for Testing Ensure is Reset ***************************
    response = (message.is_sent, message.id, str(message.sent_at))
  
while active:
    if yw_check() is not prev_check:
        print("\033[1;33;40mYellow Watch: " + yw_check())
        print(" ")
        print("\033[1;37;40m*******************************************************")
        print("")
        prev_check = yw_check()
        
    if "On Duty" in yw_check():
        yw_active = True
    else:
        yw_active = False

    # Open Raw Data from RTL_FM and MULTIMON-NG
    try:
        raw = open('raw.txt', 'r')
        #raw = open('Testing/raw.txt', 'r') # Testing
    except:
        print("Error: Ensure RTL_FM Raw Data is being piped")
    # Main Data Handling
    file = []
    for i in raw:
        file.append(i)
    for i in file:
        tts = ""
        msg = ""
        print(i)