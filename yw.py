import time
import holidays
from datetime import datetime

#Testing
test = True

#Initialise Variables for Yellow Watch.
yw_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
yw_start = '14:59:30'
yw_end = '17:25:00'
yw_holidays = []
prev_check = ""

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

while True:
    if yw_check() is not prev_check:
        print("\033[1;33;40mYellow Watch: " + yw_check())
        print(" ")
        print("\033[1;37;40m*******************************************************")
        print("")
        prev_check = yw_check()