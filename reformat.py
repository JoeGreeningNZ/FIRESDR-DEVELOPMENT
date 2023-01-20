import os
try:
    raw = open('abbr.txt', 'r')
except:
    print("Error")
file = []
newfile = []
for i in raw:
    file.append(i)
total = 0
for i in file:
    #i = i.replace("\t","': '",1)
    #if ":" not in i:
    #   i = i.replace(" \t","': '",1)
    #print(i+"',")
    #count = i.count(":")
    #if count == 2:
    #    print("error " + i)
    #    total = total + 1
#print(str(total))
    if len(i) > 3:
        print(i + "',")
