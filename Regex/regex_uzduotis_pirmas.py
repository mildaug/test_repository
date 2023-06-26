# http://pythex.org įkelkite tekstą:

# Buveinės adresas: Konstitucijos pr. 20A, 03502 Vilnius
# Telefonai:
# 1884 arba +370 5 268 4444 (Privatiems klientams)
# 1633 arba +370 5 268 4422 (Verslo klientams)
# Faksas: (8 5) 258 2700
# El. paštas: info@swedbank.lt
# Įmonės kodas: 112029651
# PVM mokėtojo kodas: LT120296515
# Banko sąskaita: LT55 7300 0100 0000 0036
# Banko kodas: 73000
# SWIFT kodas: HABALT22

# 1. Išrinkite visus žodžius, prasidedančius viena didžiąja raide.
# [A-ZĄČĘĖĮŠŲŪŽ][a-ząčęėįšųūž]+

# Išrinkite visus žodžius, kurie yra iš visų didžiųjų raidžių (PVM, SWIFT, HABALT22)
# [A-Z]{3,}\d*

# Parašykite šabloną trumpąjam telefono numeriui (nereikia idealaus, tiesiog išrinkite 1884 ir 1663)
# 1\d{3}\b

# Parašykite šabloną ilgąjam telefono numeriui
# \+370\s\d\s\d{3}\s\d{4}

# Parašykite šabloną fakso numeriui
# /\(\d\s\d\)\s\d{3}\s\d{4}/gm

# Parašykite šabloną, kuris tiktų ir ilgąjam telefono numeriui, ir faksui (naudokite '|' ir grupavimą)
# \+370\s\d\s\d{3}\s\d{4}|\(\d\s\d\)\s\d{3}\s\d{4}

# Parašykite šabloną banko sąskaitos numeriui
# LT\d{2}\s\d{4}\s\d{4}\s\d{4}\s\d{4}

# Parašykite šabloną PVM mokėtojo kodui
# LT\d{9}

# Išrinkite visus žodžius prieš dvitaškį
# [A-Za-ząčęėįšųūž]+:

# Parašykite paprastą šabloną el. paštui
# [a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}

# [a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6} - Tai yra nesudėtingas el. pašto šablonas. Išnagrinėkite, palyginkite su savo sukurtu.
# Nebūtina kas kartą kurti to, kas jau senai atitirbta. Internete gausu informacijos apie dažniausiai naudojamus regex šablonus. Pvz. https://digitalfortress.tech/tricks/top-15-commonly-used-regex/ - pasinagrinėkite.