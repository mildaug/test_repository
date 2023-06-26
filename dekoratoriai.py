#pirma uzduotis

import os
os.system('cls')
# class Studentas:
#     def __init__(self, vardas, pavarde, amzius):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius

#     @property
#     def pilnas_vardas(self):
#         return f"{self.vardas} {self.pavarde}"

#     @staticmethod
#     def ar_pilnametis(amzius):
#         return amzius >= 18

#     @classmethod
#     def sukurti_studenta(cls, vardas: str, pavarde: str, amzius: int):
#         return cls(vardas, pavarde, amzius)


# studentas_vienas = Studentas.sukurti_studenta("Lota", "Lotaite", 3)
# studentas_du = Studentas.sukurti_studenta("Saske", "Saskyte", 19)

# print(studentas_vienas.pilnas_vardas)  
# print(studentas_du.pilnas_vardas)

# print(Studentas.ar_pilnametis(studentas_vienas.amzius))
# print(Studentas.ar_pilnametis(studentas_du.amzius)) 

#antra uzduotis

from functools import wraps
def make_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == str:
                arg = arg.upper()
        for kwarg in kwargs:
            if type(kwarg) == str:
                kwargs[kwarg] = kwargs[kwarg].upper()
        result = func(*args, **kwargs)
        if type(result) == str:
            result = result.upper()
        return result
    return wrapper

@make_upper
def make_lower(string="Hello World"):
    print(f"making '{string}' lowercase")
    return string.lower()

print(make_lower())
print(make_lower("it works!"))
