minuter= int(input("hur många minuter ringer du i månaden?"))
if minuter <= 33:
    print("du borde välja Kontant")
elif minuter >= 66:
    print("du borde välja Plus")
elif minuter >= 33:
    print("du borde välja Normal")