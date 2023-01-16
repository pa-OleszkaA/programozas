nev = input("Adja meg a kereszt nevét:")
evszamok =int(input("Adja meg az élet korát:"))
if evszamok < 1:
    print("csecsemő")
elif evszamok < 5:
    print("kisgyerek")
elif evszamok < 12:
    print("nagygyerek")
elif evszamok < 16:
    print("nyugdíjas")
elif evszamok < 25:
    print("ifjú")
elif evszamok < 65:
    print("felnőt")
elif evszamok > 65:
    print("nyugdíjas")