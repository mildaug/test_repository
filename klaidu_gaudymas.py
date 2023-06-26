# try:
#     skaicius_vienas = int(input('Jusu skaicius: '))
#     skaicius_antras = int(input('Jusu skaicius: '))
#     rezultatas = skaicius_vienas / skaicius_antras
# except ZeroDivisionError:
#     print("Negalima dalyba iš nulio")
# except ValueError:
#     print("Netinkamas skaičiaus formatas")
# except:
#     print("Įvyko klaida")
# else:
#     print("Rezultatas yra:", rezultatas)


# while True:
#     try:
#         skaicius = float(input("Įveskite teigiamą skaičių: "))
#         if skaicius < 0:
#             raise ValueError("Įvestas skaičius yra neigiamas")
#         else:
#             print("Ačiū, jūs įvedėte:", skaicius)
#             break
#     except ValueError as error:
#         print("Klaida:", error)

import logging

logging.basicConfig(
    filename='logeris.log', 
    encoding='UTF-8', 
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.info('Programa veikia')
