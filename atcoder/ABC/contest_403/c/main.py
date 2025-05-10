from collections import defaultdict
from dataclasses import dataclass

@dataclass
class User:
    id: int
    is_all: bool
    access: set

n,m,q = map(int, input().split())
d = {}

# index 0 is all access
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[1] not in d:
            d[query[1]] = User(query[1], False, set())
        d[query[1]].access.add(query[2])
    elif query[0] == 2:
        if query[1] not in d:
            d[query[1]] = User(query[1], False, set()) 
        d[query[1]].is_all = True
    else:
        if query[1] not in d:
            d[query[1]] = User(query[1], False, set())
        if d[query[1]].is_all:
            print("Yes")
        else:
            if query[2] in d[query[1]].access:
                print("Yes")
            else:
                print("No")

