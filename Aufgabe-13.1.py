from logging import exception

from numpy.random.mtrand import operator

dic = {}

try:

    with open("Produkte.csv", mode="r", encoding="utf-8") as data:
        while True:

            line = data.readline().strip()
            if not line:
                break

            schlussel, wert = line.split(";")

            wert = int(wert)

            if schlussel in dic:
                dic[schlussel] += wert
            else:
                dic[schlussel] = wert

except FileNotFoundError:
    print("Produkte.csv nicht gefunden")
except ValueError:
    print("Fehler: Ungültige Daten in der Datei")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")


for schlussel, wert in dic.items():
    print(schlussel, wert)

wert2 = int(input("welcher wert soll zum anpassen benutzt werden"))

print("welchen wert möchten sie ändern")
sl = input("1 Schokolade, 2 Gummi.., 3 chips")

if sl == '1':
     sl = 'Schokolade'
if sl == '2':
     sl = 'Gummibearchen'
if sl == '3':
    sl = 'chips'
else:
    print("Fehler")

operator(input("was möchten sie mit dem wert machen? + oder -"))

if operator == '+':
    dic[sl] = wert + wert2
if operator == '-':
    dic[sl] = wert - wert2
else:
    print("Fehler")

