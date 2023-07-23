# -*- coding: utf-8 -*-


Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tLNOIQFAFJsntX2obS1rDwaTjauulwag



### Užduotis 1

Susikurkite paprastą tekstinį failą su norimu tekstu. Nuskaitykite šį failą ir suskaičiuokite kiek šiame faile yra žodžių, kiek simbolių ir kiek atskirų eilučių.
"""

with open('Mano batai buvo 2.txt', encoding='utf-8') as failas:#failo atidarymas
    tekstas = failas.read()                           #failo nuskaitymas
    print(tekstas)                                    #atspausdinu del vaizdo

kiek_zodziu = tekstas.split()   #kadangi po split grazina kaip str, tai 1 zod.bus 1 elementas
kiek_simboliu = len(tekstas)    # skaiciuoja viska su tarpais net
kiek_eiluciu = tekstas.count('\n') + 1  # Eilutės skaičius yra lygus naujų linijų simbolių + 1

print("Žodžių skaičius:", len(kiek_zodziu))
print("Simbolių skaičius:", kiek_simboliu)
print("Eilučių skaičius:", kiek_eiluciu)

"""### Užduotis 2

Susikurkite tekstinį failą kuriame būtų ši informacija:

```
Audi;A4;2010;1.6
Volvo;V60;2012;1.6
Toyota;Prius;2011;1.2
```

Nuskaitykite šį failą. Kiekvieną eilutę susidėkite į žodyną (faile informacija pateikiama tokia: markė, modelis, metai, darbinis tūris), o tą žodyną įdėkite į bendrą automobilių sąrašą.

Raskite kuris automobilis naujausias.

Raskite metų vidurkį.

Raskite kurio automobilio darbinis tūris mažiausias.
"""

with open('Auto.txt') as failas: #atidarau faila
    automobiliai = []
    for eilute in failas:
        duomenys = eilute.split(';') #issiskaidau
        automobilis = {              # stringus dedu i zodynus
            'marke': duomenys[0],
            'modelis': duomenys[1],
            'metai': int(duomenys[2]),
            'darbinis_turis': float(duomenys[3])
        }
        automobiliai.append(automobilis) #pridedu i sarasa 'automobiliai'

naujausias_automobilis = max(automobiliai, key=lambda x: x['metai']) #naujausias bus kurios metai didziausi
print('Naujausias automobilis:')
print(naujausias_automobilis)

metu_vidurkis = sum(automobilis['metai'] for automobilis in automobiliai) / len(automobiliai)
print('Metų vidurkis:', metu_vidurkis)

maziausias_turis = min(automobiliai, key=lambda x: x['darbinis_turis'])
print('Automobilis su mažiausiu darbiniu tūriu:')
print(maziausias_turis)
"""### Užduotis 3

Susikurkite csv failiuką su norimais duomenimis. Nuskaitykite pasirinktą csv failiuką ir paskaičiuokite bent 2 dalykus (pvz min/max pagal kažkurį atributą, sumą, ar pan.).
"""

# bandziau daryti pagal viršutinius pavyzdzius, bet man mesdavo klaida, maždaug
#"duomenų struktūra buvo neteisingai nuskaityta iš CSV failo"
#tada išgooglinau, kad galima per import csv ir susikurti failo pavadinimo kintamaji

import csv
failo_pavadinimas = 'Imone.csv'      # nurodau failo pavadinima ir kelia(kintamaji)
duomenys = []
with open(failo_pavadinimas) as failas:      #atsidarau
    darbuotojas = csv.DictReader(failas, delimiter=';')      #nuskaitau
    for eilute in darbuotojas:
        duomenys.append(eilute)
print(duomenys)

didziausias_atlyginimas = 0      # atrenku didz.atlyginima ir paskaiciuoju visu atlyg.vidurki
visu_atlyginimu_suma = 0
visu_atlyginimu_skaicius = len(duomenys)

for eilute in duomenys:
    atlyginimas = int(eilute['Atlyginimas'])
    if atlyginimas > didziausias_atlyginimas:
        didziausias_atlyginimas = atlyginimas
    visu_atlyginimu_suma += atlyginimas

vidurkis = visu_atlyginimu_suma / visu_atlyginimu_skaicius

print(f"Didžiausias atlyginimas: {didziausias_atlyginimas}")
print(f"Visų atlyginimų vidurkis: {vidurkis}")