#FIRESDR Smart Paging - Ambulance Paging Intercept Test

import os
from subprocess import call
import pyttsx3
import time
import holidays
from datetime import datetime
from chump import Application

active = True

capcodes = {'000997818': 'FENZ FIRECALL',
            '000999059': 'SILVERDALE FIRE',
            '001234567': 'TEST',
            }

while active:
    try:
        raw = open('../raw.txt', 'r')
        #raw = open('Testing/raw.txt', 'r') # Testing
    except:
        print("Error: Ensure RTL_FM Raw Data is being piped")
    # Main Data Handling
    file = []
    for i in raw:
            file.append(i)
    modes = file.pop(0)
    #print(modes)
    for i in file:
            if "POCSAG" in i:
                POCSAG_capcode =  i.split("Address: ",1)[-1].split(" ")[0]
                for capcode, callsign in capcodes.items():
                    if capcode == POCSAG_capcode:
                        print(callsign + " " + i)
            if "FLEX" in i:
                FLEX_capcode = i.split("|")[4]
                for capcode, callsign in capcodes.items():
                    if capcode == FLEX_capcode:
                        print(callsign + " " + i)
                

