"""
a = '''Lorem ipsum dolor sit amet,

consectetur adipiscing elit,

sed do eiusmod tempor incididunt

ut labore et dolore magna aliqua.'''

print(a)
"""
"""
a = "Hello, world!"

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

"""
"""
szam = 0
for x in "banana":
    print(x)

for x in "banana":
    print(szam,x,sep="---",end='\n')
    szam = szam +1
"""
a = "Hello, world!"
    print(len(a))

txt = "The best things in life are free!"
    print("free" in txt) 

txt = "The best things in life are free!"
    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")
   
b = "hello, world!"
print(a.upper())