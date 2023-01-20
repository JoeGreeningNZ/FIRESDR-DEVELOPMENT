import holidays

yw_holidays = []

for holiday in holidays.NZ(years=[2022]).items():
    if ((holiday[0]).weekday()) > 5:
        print(holiday[1] + " " + str(holiday[0].weekday()) + " is a weekend")
    if ((holiday[0]).weekday()) <= 5:
        print(holiday[1] + " " + str(holiday[0].weekday()) + " is weekday")
        yw_holidays.append(holiday[0].strftime('%d-%m-%y'))