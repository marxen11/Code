import time
import math
x = 1
#utskrifmt av tal med 1 och 10
while x <= 10:
    print(x)
    x += 1
#utskrift av gämna tal
k = 0
while k < 10:
    k += 1
if k%2 != 0:
    print(k)
#bäräkning av suman 1 + 2 + 3 + ... + n
while True:
    n = int(input("n?, skriv ett tal mindre än eller lika med 0 för att avsluta:"))
    start = time.time()
    if n <= 0:
        break
summa = 0
l = 1
while l <= n:
    summan = somman +l
slut = time.time()
print("summan blir ",summa,". Det tog ",round(slut - start)," sekunder att räkna ut.")
