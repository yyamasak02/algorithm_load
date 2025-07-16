n: int = int(input())
a: list[int] = list(map(int, input().split()))
b: list[int] = list(map(int, input().split()))
routes: list[int] = [10**9 for _ in range(n + 1)]
previous: list[int] = [0 for _ in range(n + 1)]
routes[0] = 0
routes[1] = 0


def min_with_index(prev: int, next: int) -> tuple:
    if prev < next:
        return (False, prev)
    return (True, next)


for index in range(1, n + 1):
    flag, v = min_with_index(routes[index + 1], routes[index] + a[index - 1])
    routes[index + 1] = v
    if flag:
        previous[index + 1] = index
    if index == n - 1:
        break
    flag, v = min_with_index(routes[index + 2], routes[index] + b[index - 1])
    routes[index + 2] = v
    if flag:
        previous[index + 2] = index
# print(previous)
result = [n]
target_index = n
while target_index > 1:
    result.append(previous[target_index])
    target_index = previous[target_index]
print(len(result))
print(" ".join(map(str, result[::-1])))
