lön = 0.01
dagar = 0
total_lön = 0
while total_lön < 10**6 :
    total_lön = total_lön + lön
    lön = lön * 2
    dagar = dagar + 1
print("din total lön år ",total_lön," äfter ",dagar," dagar och din lön är ",lön,)