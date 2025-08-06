n: int = int(input())
a: list[int] = list(map(int, input().split()))
b: list[int] = list(map(int, input().split()))
routes: list[int] = [10**9 for _ in range(n + 1)]
routes[0] = 0
routes[1] = 0
for index in range(1, n + 1):
    routes[index + 1] = min(routes[index + 1], routes[index] + a[index - 1])
    if index == n - 1:
        break
    routes[index + 2] = min(routes[index + 2], routes[index] + b[index - 1])
print(routes[-1])
