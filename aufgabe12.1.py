import os

print("welchen text möchten sie ausgeben?")
eingabe=int(input("1=Zauberlehrling, 2=Ribbeck oder 3=Erlkoenig:"))

if eingabe == 3:
    data = 'Erlkoenig'
elif eingabe == 2:
    data = 'Ribbeck'
elif eingabe == 1:
    data = 'Zauberlehrling'

print(data)

try:
    with open(data + '.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(e)






