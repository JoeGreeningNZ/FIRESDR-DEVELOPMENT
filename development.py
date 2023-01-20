import time
import holidays
from datetime import datetime

prevday = ""

#Initialise Variables for Yellow Watch.
yw_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#yw_active = True
yw_start = '14:01:00'
yw_end = '17:25:00'
yw_holidays = []
#yw_prev = False

for holiday in holidays.NZ(years=[2022]).items():
    if ((holiday[0]).weekday()) <= 5:
        yw_holidays.append(holiday[0].strftime('%d-%m-%y'))
        
def yw_check(inital=False):
    #Yellow Watch Status Processing
    currday = datetime.today().strftime('%A')
    currdate = datetime.today().strftime('%D-%M-%Y')
    currtime = datetime.now().strftime("%H:%M:%S")
    if inital:
        print("Initalising Yellow Watch")
    if (currdate not in yw_holidays):
        if (currday in yw_days):
            if (currtime > yw_start and currtime < yw_end):
                yw_active == True
                if yw_active != yw_prev or inital:
                    print("\033[1;33;40mYellow Watch: \033[1;32;40mOn Duty")
                    print(" ")
                    print("\033[1;37;40m*******************************************************")
                    print("")
                    yw_prev = yw_active
            else:
                yw_active = False
                if yw_active != yw_prev or inital:
                    print("\033[1;33;40mYellow Watch: \033[1;31;40mOff Duty")
                    print(" ")
                    print("\033[1;37;40m*******************************************************")
                    print("")
                    yw_prev = yw_active
        else:
            yw_active = False
            if yw_active != yw_prev or inital:
                print("\033[1;33;40mYellow Watch: \033[1;31;40mWeekend")
                print(" ")
                print("\033[1;37;40m*******************************************************")
                print("")
                yw_prev = yw_active
    else:
        yw_active = False
        if yw_active != yw_prev or inital:
            print("\033[1;33;40mYellow Watch: \033[1;31;40mPublic Holiday")
            print(" ")
            print("\033[1;37;40m*******************************************************")
            print("")
            yw_prev = yw_active
            
yw_check(True)
while true:
    yw_check()
                