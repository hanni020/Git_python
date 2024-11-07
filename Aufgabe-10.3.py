dic = {"Cent 1:": 0, "Cent 2": 0, "Cent 5": 0, "Cent 10": 0, "Cent 20": 0, "Cent 50": 0, "EUR 1": 0, "EUR 2": 0}

rechnung=float(input("Rechnungsbetrag")) #how many to pay
gez=float(input("Gezahlter betrag")) #how many cash is given
ruck = gez - rechnung #cashback
i = int(0)
while ruck != 0:


