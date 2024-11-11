# Initialize the coin dictionary
dic = {
    "Cent 1": 0,
    "Cent 2": 0,
    "Cent 5": 0,
    "Cent 10": 0,
    "Cent 20": 0,
    "Cent 50": 0,
    "EUR 1": 0,
    "EUR 2": 0
}

# Get input for the bill amount and amount paid
rechnung = float(input("Rechnungsbetrag: "))  # Bill amount
gez = float(input("Gezahlter Betrag: "))  # Amount paid

# Calculate the cashback
ruck = gez - rechnung

# Ensure the cashback is a positive number
if ruck < 0:
    print("Gezahlter Betrag ist weniger als der Rechnungsbetrag!")
else:
    # Start counting coins
    i = 0
    while ruck > 0:
        # Round the remainder to avoid precision errors
        ruck = round(ruck, 2)

        if ruck >= 2:
            dic["EUR 2"] = int(ruck // 2)  # Use integer division to get the number of coins
            ruck -= dic["EUR 2"] * 2  # Subtract the value of the coins used

        elif ruck >= 1:
            dic["EUR 1"] = int(ruck // 1)
            ruck -= dic["EUR 1"] * 1

        elif ruck >= 0.50:
            dic["Cent 50"] = int(ruck // 0.50)
            ruck -= dic["Cent 50"] * 0.50

        elif ruck >= 0.20:
            dic["Cent 20"] = int(ruck // 0.20)
            ruck -= dic["Cent 20"] * 0.20

        elif ruck >= 0.10:
            dic["Cent 10"] = int(ruck // 0.10)
            ruck -= dic["Cent 10"] * 0.10

        elif ruck >= 0.05:
            dic["Cent 5"] = int(ruck // 0.05)
            ruck -= dic["Cent 5"] * 0.05

        elif ruck >= 0.02:
            dic["Cent 2"] = int(ruck // 0.02)
            ruck -= dic["Cent 2"] * 0.02

        elif ruck >= 0.01:
            dic["Cent 1"] = int(ruck // 0.01)
            ruck -= dic["Cent 1"] * 0.01

    # Print out the number of each coin
    for key, value in dic.items():
        if value > 0:  # Only print coins that are used
            print(f"{key}: {value}")
