#pirma uzduotis

# import random

# def skaiciai_is_eiles():
#     skaiciai = [random.randint(1, 100) for _ in range(10)]
#     is_eiles = sorted(skaiciai)
#     print(is_eiles)

# skaiciai_is_eiles()

#antra uzduotis

# import random
# i = 0
# while (i < 3):
#     kauliukas = random.randint(1, 6)
#     print(kauliukas)
#     if kauliukas == 5:
#         print("pralaimejai")
#         break
#     i = i + 1
# else:
#     print("laimejai")

#trecia uzduotis
import calendar

def spausdinti_menesio_kalendoriu_suskaiciuojant_savaitgalius(metai, menesis):
    print(calendar.month(metai, menesis))

    _, menesio_ilgis = calendar.monthrange(metai, menesis)

    savaitgalio_dienos = 0
    for diena in range(1, menesio_ilgis + 1):
        savaites_diena = calendar.weekday(metai, menesis, diena)
        if savaites_diena == 5 or savaites_diena == 6:
            savaitgalio_dienos += 1

    print(f"Savaitgalio dienų skaičius šiame mėnesyje: {savaitgalio_dienos}")

# Pavyzdys su 2023-ųjų balandžio mėnesiu
spausdinti_menesio_kalendoriu_suskaiciuojant_savaitgalius(2023, 4)