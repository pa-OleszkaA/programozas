egyikszam=int(input("Kérem az elsö számot 1-00-ig"))
masikszam=int(input("Kérem az masik számot 1-00-ig"))
if egyikszam==masikszam:
    print('megegyezik')
elif  egyikszam>masikszam:
    print("az első szám nagyobb" , egyikszam-masikszam, "nagyobb")
    print("ennyivel:",egyikszam-masikszam)
else:
    print("megegyezik")
        