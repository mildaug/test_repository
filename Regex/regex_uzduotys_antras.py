import re

# Parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd. Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu.

def date_format(date):
    pattern = re.compile(r'^(\d{2})\.(\d{2})\.(\d{4})$')
    res = pattern.sub('\g<3> \g<2> \g<1>', date)
    return res

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

pattern = re.compile(r'[A-Z]\w+ \d{1,2}, 20\d{2}')
res = pattern.findall(text)
print(res)