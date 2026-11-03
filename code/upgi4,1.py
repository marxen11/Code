största_tal = 0
minsta_tal = float("inf")
while True:
    tal = int(input("välj et tal"))
    if tal < 0:
        break
    if tal > största_tal:
        största_tal = tal
    if tal < minsta_tal:
        minsta_tal = tal
print("det största talet är ",största_tal,"och det minsta är",minsta_tal,)