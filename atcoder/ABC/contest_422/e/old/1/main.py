from math import gcd


def line_equation(x1, y1, x2, y2):
    a = y1 - y2
    b = x2 - x1
    c = -(a * x1 + b * y1)
    g = gcd(gcd(abs(a), abs(b)), abs(c))
    if g > 0:
        a //= g
        b //= g
        c //= g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


if __name__ == "__main__":
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    ans = {}
    prev = None
    for i in range(n - 1):
        res = line_equation(*coords[i], *coords[i + 1])
        if res not in ans:
            ans[res] = 0
        ans[res] += 1 if res == prev else 2
        prev = res

    for key, value in ans.items():
        if value >= n // 2 + 1:
            print("Yes")
            print(*key)
            break
    else:
        print("No")
