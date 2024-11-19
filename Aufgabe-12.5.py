vorname=input("Bitte geben sie ihren vornamen ein")
nachname=input("Bitte geben sie ihren Nachname ein")
strase=input("Bitte geben sie ihre Strase ein")
hausnummer=input("Bitte geben sie ihre Hausnummer ein")
PLZ=input("Bitte geben sie ihre PLZ ein")
name=input("wie wollen sie die datei nennen")

gesamt =(f"{vorname} {nachname} {strase} {hausnummer} {PLZ}")

try:
    stream =open(f"{name}.txt", mode="wt", encoding="utf-8")

    stream.write(gesamt)

    stream.close()
except Exception as ex:
    print(ex)
