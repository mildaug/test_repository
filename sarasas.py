#pirma uzduotis

sarasas = [10, 20, 30, 40, 50, 60]

# result = map(lambda x: x * 2, filter(lambda x: x > 10, sarasas))
# print(list(result)) 

#antra uzduotis

# from functools import reduce
# import operator

# suma = reduce(lambda x, y: x * y, sarasas)
# print(suma)

#trecia uzduotis

# import statistics

# print(sum(sarasas))
# print(max(sarasas))
# print(min(sarasas))
# print(statistics.mean(sarasas))
# print(statistics.median(sarasas))

#ketvirta uzduotis

# rusiuoti_skaiciai = sorted(sarasas, key=lambda x: x % 3)
# print(rusiuoti_skaiciai)

#penkta uzduotis

import os
from functools import reduce

os.system('cls')

vidurkis = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, sarasas)) / len(list(filter(lambda x: x % 2 == 0, sarasas)))
print(vidurkis) 
