r, x = map(int, input().split())
if x == 1:
    if r >= 1600 and r <= 2999:
        print("Yes")
    else:
        print("No")
else:
    if r >= 1200 and r <= 2399:
        print("Yes")
    else:
        print("No")