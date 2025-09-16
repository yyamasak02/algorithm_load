query = sorted(list(map(int, input().split())))
if query[0] * query[1] == query[2]:
    print("Yes")
else:
    print("No")
