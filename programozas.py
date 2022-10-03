#1. feladat 9dk
IDEI_ÉV = 2022
print(type(IDEI_ÉV))
print('Az IDEI_ÉV változó értéke: ', IDEI_ÉV, sep='--->')
felhasználó_kora = input('Hány éves vagy?')
print(type(felhasználó_kora))
print('Te most', felhasználó_kora,'éves vagy.')
felhasználó_kora = int(felhasználó_kora)
születési_év = IDEI_ÉV - felhasználó_kora
print('Ekkor születtél: ', születési_év, '.', sep='')

