zahl1=int(input("bitte geben sie eine zahl ein"))

zahl2=int(input("bitte geben sie eine zweite zahl ein"))

op=int(input("1=plus, 2=minus, 3=mal, 4=geteilt"))

try:
    if op == 1:
        erg = zahl1 + zahl2
    elif op == 2:
        erg = zahl1 - zahl2
    elif op == 3:
        erg = zahl1 * zahl2
    elif op == 4:
        erg = zahl1 / zahl2

    print(erg)

except:
    print("fehler")