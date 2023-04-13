#print('God dag') # komentaro testas
#print('God morgen')
#print('God dag til deg')
#print ('Labas')

#a = 1
#b = 101.1
#c = 'Pasaulis'
#print(type(a),a)
#print(type(b), b)
#print(type(c), c)

#x = 2
#y = 3
#z = 4
#atsakymas1 = x + y
#atsakymas2 = x - y
#atsakymas3 = x * y * y
#atsakymas4 = x / y
#atsakymas5 = x ** y
#print(atsakymas1, atsakymas2, atsakymas3, atsakymas4, atsakymas5)

#x = z
#atsakymas1 = x + y
#atsakymas2 = x - y
#atsakymas3 = x * y * y
#atsakymas4 = x / y
#atsakymas5 = x ** y
#print('atsakymas1 ', atsakymas1, ',', 'atsakymas2 ', atsakymas2, 'atsakymas3 ', atsakymas3, 'atsakymas4 ', atsakymas4, 'atsakymas5', atsakymas5)

#atsakymas1 = x + z
#atsakymas2 = x - z
#atsakymas5 = x ** z
#atsakymas3 = x * z * z
#atsakymas4 = x / z
#print(atsakymas1, atsakymas2, atsakymas3, atsakymas4, atsakymas5)

#a = 11
#b = 10
#if a > 5 and b < 10:
    #print('Abu teiginiai teisingi')
#elif a > b or b < 10:
    #print('Bent vienas teiginys yra teisingas')
#else:
    #print('Abu teiginiai neteisingi')


#amžius = int(input('Įveskite amžių: '))
#if amžius >= 18:
    #print('Jūs esate pilnametis')
#else:
    #print ('Jūs esate nepilnametis')

#skaičius = int(input('Įveskite skaičių: '))
#if skaičius >= 0:
    #print('Skaičius teigiamas')
#else:
    #print ('Skaičius neigiamas')

#skaičius = int(input('Įveskite skaičių: '))
#if skaičius >=5:
    #if skaičius <=10:
        #print('Skaičius yra tarp 5 ir 10')
#else:
    #print ('Skaičius nėra tarp 5 ir 10')


#skaičius_a = int(input("Įveskite skaičių: "))
#skaičius_b = int(input("Įveskite skaičių: "))

#if skaičius_a > 0 and skaičius_b > 0:
    #print("Abu skaičiai yra didesni nei 0")
#else:
    #print("Bent vienas skaičius yra neigiamas arba lygus 0")


#a = int(input("Įveskite pirmą skaičių: "))
#b = int(input("Įveskite antrą skaičių: "))

#if a % 2 == 0 or b % 2 == 0:
    #print("Bent vienas skaičius yra lyginis")
#else:
    #print("Abu skaičiai yra nelyginiai")


#Paprašome įvesti bet kokią eilutę
#eilutė = input('Įveskite eilutę: ')
#print(eilutė[0])
#print(eilutė[-1])

#knyga = 'Haris Poteris'
#print(knyga [0:5])

#citata = 'Karčios šaknys, saldūs vaisiai'
#print(citata[-3:])

#pirmas_zodis = input("Įveskite pirmąjį žodį: ")
#antras_zodis = input("Įveskite antrąjį žodį: ")
#print(pirmas_zodis[0] + "-" + antras_zodis[0])

#įvestis
#pirmas_žodis = input('Įvesti pirmą žodį: ')
#antras_žodis = input('Įvesti antrą žodį: ')
#print(pirmas_žodis[0] + "-" + antras_žodis[0])

#skaicius = int(input('Jūsų skaičius: '))
#if skaicius > 5 and skaicius < 10:
    #print('Jūsų skaičius didesnis už 5, bet mažesnis už 10')
#else:
    #print('Jūsų skaičius mažesnis už 5 ir mažesnis už 10')

#print("Labas")

#atlyginimas = input("Įveskite atlyginimą: ")
#mokestis = input("Įveskite mokesčio procentą: ")
#atlyginimas_po_mokesciu = int(atlyginimas) * (1 - int(mokestis) / 100)
#print(f"Jūsų atlyginimas į rankas yra: {atlyginimas_po_mokesciu:.2f} EUR")

#print("God dag")

vardas = input("Įveskite savo vardą: ")
metai = input("Įveskite savo amžių: ")
metai_iki = 100 - int(metai)
rezultatas = 2023 + metai_iki
print(f"Sveiki, {vardas}! Jums sukaks 100 metų {rezultatas}.")