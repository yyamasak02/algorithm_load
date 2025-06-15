n,q = map(int, input().split())
array = [i for i in range(1, n+1)]
offset = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        array[(offset + query[1]-1) % n] = query[2]
    elif query[0] == 2:
        print(array[(offset + query[1]-1) % n])
    else:
        offset += query[1]
