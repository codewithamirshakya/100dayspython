import time

hh = int(time.strftime("%H"))
print(hh)

if (hh >= 6 and hh <=12):
    print("Good morning")
elif (hh >= 12 and hh <=18):
    print("Good afternoon")
elif (hh >= 18 and hh <= 20):
    print("Good evening")
else:
    print("Good night")