data = 'Namen.txt'
ar = []
i = 0
try:
    with open(data, 'r') as file:
        i = i + 1
        while True:
            content = file.readline()
            ar.append(content.strip())
            if not content:
                file.close()
                break

except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')
except Exception as e:
    print(f"An error occurred: {e}")

n = len(ar)
for i in range(n):
    for j in range(0, n-i-1):
        if ar[j] > ar[j+1]:
            ar[j], ar[j+1] = ar[j+1], ar[j]

k = len(ar)
for i in range(k):
    print(ar[i])



