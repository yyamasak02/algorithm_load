import sys

sys.set_coroutine_origin_tracking_depth(10**9)


def dfs(idx, sz, val):
    for i in range(sz + 1):
        val ^= s[i]
        s[i] += a[idx]
        val ^= s[i]
        if idx == n - 1:
            results.add(val)
        elif i < sz:
            dfs(idx + 1, sz, val)
        else:
            dfs(idx + 1, sz + 1, val)
        val ^= s[i]
        s[i] -= a[idx]
        val ^= s[i]
    return


if __name__ == "__main__":
    global n, a, s, val, results
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * n
    val = 0
    results = set()
    dfs(0, 0, val)
    print(len(results))
