
#pirma uzduotis
aibe_pirma = {11, 2, 33, 4, 55}
print(aibe_pirma)
aibe_pirma.add(6)
print(aibe_pirma)

#antra uzduotis
aibe_antra = {11, 22, 33, 44, 55}
print(aibe_antra)
aibe_antra.remove(55)
print(aibe_antra)

#trecia uzduotis
bendra_aibe = aibe_pirma.intersection(aibe_antra)
print(bendra_aibe)

#ketvirta uzduotis
aibiu_skirtumai = aibe_pirma.difference(aibe_antra)
print(aibiu_skirtumai)

#penkta uzduotis
aibiu_skirtumai_galutinis = aibe_antra.difference(aibe_pirma)
print(aibiu_skirtumai_galutinis)

#BONUS

for skaicius in aibiu_skirtumai_galutinis:
    print(skaicius ** 2)