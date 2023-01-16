#Bekérünk két egész számot és irassuk ki a nagyobb számot
"""
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("kérek egy másik számot: "))
if szam1 > szam2:
    print("A szam1 naygobb mint a szam2 ")
else: 
    print("A szam2 kisebb mint a szam1" )  
    
    """

"""
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("kérek egy másik számot: "))
if szam1 > szam2:
    print("A szam1 naygobb mint a szam2 " )
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1" )
else:
     print("szam1 megeggyezik a szam2-vel" )

"""

a=int(input("Kérek egy egész számot: "))
b=int(input("Kérek egy egész számot: "))
c=int(input("Kérek egy egész számot: "))
if  a < b and c > b:
    print("a<b és c>b")
else:
    print("A feltétel hamis")