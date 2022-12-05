# A pyhton lista

# A listák több elem tárolására szolgálnak egyetlen változóban
# A listákat szögletes zárójelekkel hozzuk létre:
# Példa:
lista = ["alma", "banán", "cseresznye"]
print(lista)

lista = ["alma", "banán", "cseresznye", "alma", "banán"]
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista = ["alma", "banán", "cseresznye"]
print(len(lista))
hossza = len(lista)
print(hossza)

# A listaelemek bármilyen adattípusúak lehetnek:
# Példa:
lista1 = ["alma", "banán", "cseresznye"]
lista2 = [1, 5, 7, 9, 3]
lista3 = [True, False, False]
print(lista2)

lista = list (("alma", "banán", "cseresznye"))
print(lista)

# Írassuk ki a lista utolsó elemét
lista = ["alma", "banán", "cseresznye"]
print(lista[-1])

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőllő-5", "mangó-6"]
print(lista[2:5])

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőllő-5", "mangó-6"]
print(lista[2:])
újlista = lista[2:]
print(újlista) 

lista_10D_1csop = ["FB", "GM", "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SR", "SM2", "TP", "TS", "TT",]
print(lista_10D_1csop)

lista_1csop = ["FB", "GM", "HK", "KG", "MM"]
print(lista_1csop)

lista_2csop = ["OA", "PJ", "PP", "SP"]
print(lista_2csop)

lista_3csop = ["SR", "SM2", "TP", "TS", "TT"]
print(lista_3csop)

#------------------------------------------------------------------------------------------
lista_10D_1csop = ["FB", "GM", "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SR", "SM2", "TP", "TS", "TT",]
print(lista_10D_1csop)


csop1 = lista_10D_1csop[0:5]
csop2 = lista_10D_1csop[5:10]
csop3 = lista_10D_1csop[10:14]
print(csop1)
print(csop2)
print(csop3)
