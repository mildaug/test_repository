# def pasisveikinimas(vardas):
#     print(f"Labas {vardas}")

# pasisveikinimas ("Studente")
# pasisveikinimas ("Milda")

# #pirma uzduotis
# def lyginis_nelyginis(skaicius):
#     if skaicius % 2 == 0:
#         print("Įvestas skaičius yra lyginis.")
#     else:
#         print("Įvestas skaičius yra nelyginis.")

# lyginis_nelyginis(10)
# lyginis_nelyginis(5)

# #antra uzduotis
# def ar_teigiamas(skaicius):
#     if skaicius > 0:
#         print("Įvestas skaičius yra teigiamas.")
#     else:
#         print("Įvestas skaičius nėra teigiamas.")

# ar_teigiamas(-1)
# ar_teigiamas(3)

# #trecia uzduotis

# skaicius = int(input('Iveskite skaiciu: '))
# riba = int(input('Iveskite riba: '))
# def ar_daugiau_nei(skaicius, riba):
#     if skaicius > riba:
#         print(f"Įvestas skaičius yra didesnis nei {riba}.")
#     else:
#         print(f"Įvestas skaičius nėra didesnis nei {riba}.")

# ar_daugiau_nei(skaicius,riba)

# def atbulai(tekstas):
#     return (tekstas[::-1])

# print(atbulai("labas"))

# def kvadratu(x):
#     return x**2

# print(kvadratu(4))

#pirma uzduotis
# sarasas = ['migdolai', 'anakardziai', 'lazdynai']
# def sarasas_atvirksciai (sarasas):
#     return (sarasas[::-1])

# print(sarasas_atvirksciai(sarasas))

# sarasas = ('migdolai')
# def sarasas_atvirksciai (sarasas):
#     return (sarasas[::-1])

# print(sarasas_atvirksciai(sarasas))

#antra uzduotis
#a ** 2 + b ** 2 = c **2

# def trikampio_plotas (a, b):
#     plotas = a ** 2 + b ** 2
#     plotas_istraukta_saknis = plotas ** 1/2
#     return plotas_istraukta_saknis

# a = int(input('Krastine a: '))
# b = int(input('Krastine b: '))

# plotas = trikampio_plotas(a, b)

# print(plotas)

#trecia uzduotis

# def zodziai_pagal_ilgi(sakinys, ilgis):
#     zodziai = sakinys.split()
#     zodzio_ilgis = []
#     for zodis in zodziai:
#         if len(zodis) == ilgis:
#             zodzio_ilgis.append(zodis)
#     return zodzio_ilgis

# sakinys = "A court of thorns and roses"
# ilgis = 2
# zodziai = zodziai_pagal_ilgi(sakinys, ilgis)

# print(zodziai)


#ketvirta uzduotis
# def didziausias_skaicius(skaiciai):
#     didziausias = skaiciai[0]
#     for skaicius in skaiciai:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias

# skaiciai = [4, 2, 7, 1, 9, 5]
# didziausias = didziausias_skaicius(skaiciai)
# print(didziausias)

# #penkta uzduotis
# def rinkti_zodzius_pagal_raide(zodziai, raide):
#     raides_zodziai = []
#     for zodis in zodziai:
#         if zodis[0] == raide:
#             raides_zodziai.append(zodis)
#     return raides_zodziai

# zodziai = ["automobilis", "arklys", "avokadas", "bananas", "briedis"]
# raide = "a"
# a_zodziai = rinkti_zodzius_pagal_raide(zodziai, raide)
# print(a_zodziai)

# #sesta uzduotis
# def rinkti_lyginio_ilgio_zodzius(tekstas):
#     zodziai = tekstas.split()
#     lyginio_ilgio_zodziai = []
#     for zodis in zodziai:
#         if len(zodis) % 2 == 0:
#             lyginio_ilgio_zodziai.append(zodis)
#     return lyginio_ilgio_zodziai

# tekstas = "Labas Vakare, kaip sekasi?"
# lyginio_ilgio_zodziai = rinkti_lyginio_ilgio_zodzius(tekstas)
# print(lyginio_ilgio_zodziai) 

# def skaiciuoti_kaina(prekes_pavadinimas, kaina, nuolaida=0, pvm=21):
#     kaina_su_nuolaida = kaina * (1 - nuolaida / 100)
#     kaina_su_pvm = kaina_su_nuolaida * (1 + pvm / 100)
#     print(f"{prekes_pavadinimas} - kaina su nuolaida ir PVM: {kaina_su_pvm:.2f}€")

# def apskritimo_plotas(r, pi=3.14):
#     plotas = pi * (r ** 2)
#     return plotas

# print(apskritimo_plotas(3))

# def keliones_info(keliones_trukme, greitis, vartojimas=7, kuro_kaina=1.2):
#     atstumas = keliones_trukme * greitis
#     kuro_sanaudos = atstumas * vartojimas / 100
#     islaidos = kuro_sanaudos * kuro_kaina

#     return {
#         atstumas, 
#         kuro_sanaudos, 
#         islaidos

#     }

# print(keliones_info(3,90))

#pirma uzduotis
# def didziausias(*args):
#     didziausias_skaicius = args[0]
#     for arg in args:
#         if arg > didziausias_skaicius:
#             didziausias_skaicius = arg
#     return didziausias_skaicius

# print(didziausias(1, 4, 7, 9,7))
# print(didziausias(4, 14, 6, 9))

#antra uzduotis
def raktai(**kwargs):
    nurodyti_raktai = {}
    for key in kwargs:
        if key in ["vardas", "amzius", "miestas", "metai"]:
            nurodyti_raktai[key] = kwargs[key]
    return nurodyti_raktai

print(raktai(vardas="Jonas", amzius=30, miestas="Vilnius", metai=2023))  # {'vardas': 'Jonas', 'amzius': 30, 'miestas': 'Vilnius'}
print(raktai(pavadinimas="Python"))

#trecia uzduotis
def sujungtas_sarasas(*args, **kwargs):
    visi_elementai = list(args)
    visi_elementai += list(kwargs.values())
    return visi_elementai
