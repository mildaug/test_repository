#pirma uzduotis

# with open("pakeitimai.txt", "r") as failas:
#     eilute = failas.readline()
#     print(eilute)
#     pakeista_eilute = eilute.swapcase()
#     print(pakeista_eilute)

#antra uzduotis

# with open("skaiciai.txt", "w") as failas:
#     for skaicius in range(1, 101):
#         failas.write(f"{skaicius}\n")

#trecia uzduotis

# with open("tekstas.txt", "r") as failas:
#     failas.seek(0, 2) 
#     failo_ilgis = failas.tell()  
#     vidurys = failo_ilgis // 2  

#     failas.seek(vidurys)  
#     likusi_dalis = failas.read()  
#     print(likusi_dalis)

#ketvirta uzduotis

with open("eilutes.txt", "w", encoding="utf-8") as failas:
    failas.write("Saulėlydis žėri žemę švelniai.\n")
    failas.write("Vakare vėjas šnypščia medžius.\n")
    failas.write("Vėjas nerimsta, šnypščia ir švilpia.\n")

with open("eilutes.txt", "a", encoding="utf-8") as failas:
    failas.write("Milda Auglyte\n")

with open("eilutes.txt", "r", encoding="utf-8") as failas:
    for eilute in failas:
        if "vėjas" in eilute:
            print(eilute)


