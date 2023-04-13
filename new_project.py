
#Naujas projektas vabalui atpažinti
print("Sveiki prisijungę prie programėlės, kuri jums padės atpažinti jūsų matytą vabalą!")

#Paprašome įvesti vabalo spalvą ir specifikacijas
choice_klase = input("Pasirinkite spalvą: 1 - žalias, 2 - mėlynas, 3 - raudonas: ")
if choice_klase == "1":
    choice_specifikacija = input("Pasirinkite vabalo specifikacijas: 1 - ilgos antenos, 2 - kvadratiškas kūnas: ")
    if choice_specifikacija == "1":
        print("Jūsų matytas vabalas: Muskusinis kvapūnas")
    if choice_specifikacija == "2":
        print("Jūsų matytas vabalas: Paprastasis auksavabalis")
elif choice_klase == "2":
    choice_specifikacija = input("Pasirinkite vabalo specifikacijas: 1 - pailgas ir ryškiai segmentuotas kūnas, 2 - apvalus kūnas: ")
    if choice_specifikacija == "1":
        print("Jūsų matytas vabalas: Paprastasis gegužvabalis")
    if choice_specifikacija == "2":
        print("Jūsų matytas vabalas: Paprastasis mėšlavabalis")
elif choice_klase == "3":
    choice_specifikacija = input("Pasirinkite vabalo specifikacijas: 1 - juodai ir raudonai dryžuotas kūnas, 2 - nedidelis ir skleidžia cypimą primenančius garsus: ")
    if choice_specifikacija == "1":
        print("Jūsų matytas vabalas: Juostuotoji skydblakė")
    if choice_specifikacija == "2":
        print("Jūsų matytas vabalas: Lelijinis lapagraužis")
else:
    print("Pasirinkimas neteisingas")