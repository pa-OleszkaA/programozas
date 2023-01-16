nev = input('Adja meg a keresztnevét: ')
evszam= int(input('Adja meg az élet korát: '))
if evszam < 1:
    print(nev, "csecsemő!")
elif evszam < 6:
    print(nev, "kisgyerek!")
elif evszam < 12:
    print(nev, "gyerek!")
elif evszam < 16:
    print(nev, "serdülő!")
elif evszam < 25:
    print(nev, "ifjú!")
elif evszam < 65:
    print(nev, "felnőtt!")
elif evszam >= 65:
    print(f"A kora alapján {nev} nyugdíjas!")
