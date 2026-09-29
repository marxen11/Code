import math
sida_A = int(input("Hur lång är sida A?"))
sida_B = int(input("Och hur lång är sida B?"))
vinkel_avAoB = int(input("Vad är vinkeln?"))
sida_C = math.sqrt(sida_A**2 + sida_B**2 - (2 * sida_A * sida_B * math.cos(vinkel_avAoB)))
print (sida_C)
if sida_A == sida_B == sida_C:
    print("triangeln är liksidig")
elif sida_A == sida_B or sida_B == sida_C or sida_A == sida_C:
    print("triangeln är lickbent")
else:
    print("ful ahh triangel")