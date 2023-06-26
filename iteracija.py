import os
os.system('cls')

#pirma uzduotis

# sarasas = [1, 2, 3, 4, 5]
# for elementas in sarasas:
#     if elementas % 2 == 0:
#         print(elementas)

#antra uzduotis

# zodynas = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}
# iteratorius = iter(zodynas.items())

# while True:
#     try:
#         raktas, reiksme = next(iteratorius)
#         if reiksme > 4:
#             print(raktas, reiksme)
#     except StopIteration:
#         break

# trecia uzduotis

# tekstas = 'The filters are consulted in turn, until one of them returns a false value.'
# ilgiai = (len(zodis) for zodis in tekstas.split())

# for ilgis in ilgiai:
#     print(ilgis)

#ketvirta uzduotis

def pirminiai(n):
    pirminis = [True] * (n+1)
    pirminis[0] = pirminis[1] = False
    for i in range(2, int(n**0.5)+1):
        if pirminis[i]:
            for skaicius_vienas in range(i*i, n+1, i):
                pirminis[skaicius_vienas] = False
    return [skaicius_antras for skaicius_antras in range(n+1) if pirminis[skaicius_antras]]
print(pirminiai(100))