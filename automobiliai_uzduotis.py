import sqlite3
conn = sqlite3.connect("autouzduotis.db")
c = conn.cursor()

create_query = """CREATE TABLE IF NOT EXISTS automobiliai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    automobilio_marke VARCHAR(50),
    modelis VARCHAR(50),
    spalva VARCHAR(50),
    pagaminimo_metai VARCHAR(50),
    kaina VARCHAR(50)
);"""

c.execute(create_query)
conn.commit()

while True:
    print("""Automobiliu sarasas:
    1 - Ivesti nauja automobili
    2 - Paieska
    0 - Iseiti
    """)

    choice = input("Pasirinkite: ")
    if choice == "1":
        automobilio_marke = input("Automobilio marke: ")
        modelis = input("Automobilio modelis: ")
        spalva = input("Automobilio spalva: ")
        pagaminimo_metai = input("Automobilio pagaminimo metai: ")
        kaina = input("Automobilio kaina: ")
        with conn:
            c.execute("""INSERT INTO automobiliai 
            (automobilio_marke, modelis, spalva, pagaminimo_metai, kaina) 
            VALUES(?, ?, ?, ?, ?)""", (automobilio_marke, modelis, spalva, pagaminimo_metai, kaina))
        print(f"{automobilio_marke} ivestas.")

    elif choice == "2":
        automobilis = input("Automobilio marke: ")
        with conn:
            c.execute('SELECT rowid, * FROM automobiliai WHERE automobilio_marke = ?', (automobilis))
            automobiliai = c.fetchall()

        if automobiliai and len(automobiliai) > 0:
            for automobilis in automobiliai:
                print(automobilis)
        else:
            print("Automobilis nerastas")
    elif choice == "0":
        break

c.close()