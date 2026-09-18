mätarställningen_idag= int(input("mätarställningen idag?"))
mätarställningen_ett_år= int(input("mätarställningen för ett år?"))
antal_mil= mätarställningen_idag-mätarställningen_ett_år
print(antal_mil)
antal_liter_bensin= int(1235.4)
antal_körda_mil= int(1487)
förbrukning_pär_mil= antal_liter_bensin/antal_körda_mil
print(f'{förbrukning_pär_mil:.2}')