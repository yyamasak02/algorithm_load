n = [0 for i in range(101)]
q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        n[query[1]] += 1
    else:
        for i in range(101):
            if n[i] > 0:
                print(i)
                n[i] -= 1
                break
