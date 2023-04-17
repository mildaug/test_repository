
#pirma uzduotis
grupes_1 = ('Igorr', 'Moderat', 'Kiss', 'Skid Row')
print(grupes_1)

#antra uzduotis
grupes_2 = ('Muse', 'Slipknot', 'Dua Lipa')
print(grupes_2)

#trecia uzduotis
print(grupes_1[0])
print(grupes_2[1])
print(grupes_2[-1])
grupes_bendras = grupes_1 + grupes_2
print(grupes_bendras)

#ketvirta uzduotis
print(grupes_bendras[::2])

#penkta uzduotis
print(grupes_bendras.count('Dua Lipa'))
print(grupes_bendras.index('Dua Lipa'))
print('Dua Lipa' in grupes_bendras)
print(type(grupes_bendras))
