
def solve(n, a) -> int:
    ans = n + 2
    d = {}
    for i in range(n):
        if not d.get(a[i], None):
            d[a[i]] = [i]
        else:
            ans = min(ans, i - d[a[i]][-1] + 1)
            d[a[i]].append(i)
    return -1 if ans == n + 2 else ans
        


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans)