a, b = map(int , input().split())

res = a / b
nokori = float(a // b)

if res - nokori >= 0.5:
    print(int(nokori + 1))
else:
    print(int(nokori))

