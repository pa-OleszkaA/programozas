class Eroller:
    def __init__(self, marka, seb, telj) -> None:
        self.marka = marka 
        self.maxseb = int(seb)
        self.teljesitmeny = int(telj)

    def ToString(self):
        kimenet = f"A roller márkája: {self.marka}\n"
        kimenet += f"maximális sebessége: {self.maxseb} km/h\n"
        kimenet += f"teljesítmény: {self.teljesitmeny} w"
        return kimenet

ujRoller1 = Eroller("Akai F10",25,250)
print(ujRoller1.ToString())

ujRoller2 = Eroller("Akai F15",45,450)
print(ujRoller2.ToString())

ujRoller13 = Eroller("Akai F10",50,500)
print(ujRoller13.ToString())

print(f"Az ujRoller1 objektum neve: {ujRoller1.marka}")
print(f"Az ujRoller2 objektum neve: {ujRoller2.marka}")
print(f"Az ujRoller13 objektum neve: {ujRoller13.marka}")


kiirszoveg = ujRoller1.marka+'\n' + ujRoller2+'\n' + ujRoller13+'\n'
print(kiirszoveg)
with open ('marka.txt', 'w', encoding='utf-8') as markanev:
    markanev.write(kiirszoveg)