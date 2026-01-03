query: str = input()
i: int = int(query[0])
j: int = int(query[2])

if j < 8:
    print(f"{i}-{j+1}")
else:
    print(f"{i+1}-{1}")
