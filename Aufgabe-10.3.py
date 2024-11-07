dic = {"Cent 1:": 1, "Cent 2": 2, "Cent 5": 5, "Cent 10": 10, "Cent 20": 20, "Cent 50": 50, "EUR 1": 100, "EUR 2": 200}

rechnung=float(input("Rechnungsbetrag"))
gez=float(input("Gezahlter betrag"))
ruck = gez - rechnung
i = int(0)
while ruck != 0:
    for key in dic.keys():
        print(f"{key}:{i}")
