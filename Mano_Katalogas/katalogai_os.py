#pirma uzduotis

import os

katalogo_kelias = 'Mano_Katalogas'
if not os.path.exists(katalogo_kelias):
    os.makedirs(katalogo_kelias)
    print(f"Katalogas '{katalogo_kelias}' sukurtas.")
else:
    print(f"Katalogas '{katalogo_kelias}' jau egzistuoja.")

#antra uzduotis

dabartinis_katalogas = os.getcwd()
print(f"Dabartinis katalogas: {dabartinis_katalogas}")

print("Failai ir katalogai:")
for elementas in os.listdir(dabartinis_katalogas):
    print(elementas)

#trecia uzduotis

failo_kelias = "testas.txt"

with open(failo_kelias, "w") as f:
    f.write("Tai yra testinis failas.")

if os.path.exists(failo_kelias):
    os.remove(failo_kelias)
    print(f"Failas '{failo_kelias}' ištrintas.")
else:
    print(f"Failas '{failo_kelias}' neegzistuoja.")