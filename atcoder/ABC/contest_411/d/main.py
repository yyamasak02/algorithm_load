from collections import deque

n: int = None
q: int = None
query: list[any] = None

n, q = map(int, input().split())
server: list = []
requests: deque[tuple[int, int, any]] = deque()

for i in range(q):
    query = input().split()
    if query[0] == "1":
        requests.append((int(query[0]), int(query[1]), ""))
    elif query[0] == "2":
        requests.append((int(query[0]), int(query[1]), query[2]))
    else:
        requests.append((int(query[0]), int(query[1]), ""))

same_number: int = None
while requests:
    query = requests.pop()
    if same_number is None:
        if query[0] == 3:
            same_number = query[1]
    elif query[1] == same_number:
        if query[0] == 1:
            same_number = None
        elif query[0] == 2:
            server.append(query[2])
        else:
            same_number = query[1]
result = "".join(reversed(server))
print(result)
