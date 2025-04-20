N, M = map(int, input().split())
dish_needs = []  
dishes = {j+1: [] for j in range(N)}
unavailable_count = [0] * M
counter = M
is_disliked = [False] * (N + 1)
result = [0] * N

for i in range(M):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    ingredients = tmp[1:]
    dish_needs.append(set(ingredients))
    for j in ingredients:
        dishes[j].append(i)
B = list(map(int, input().split()))
for i in range(N - 1, -1, -1):
    result[i] = counter
    ing = B[i]
    is_disliked[ing] = True
    for j in dishes[ing]:
        if unavailable_count[j] == 0:
            counter -= 1
        unavailable_count[j] += 1
for r in result:
    print(r)