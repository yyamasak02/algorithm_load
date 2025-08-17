def check(arr, n, m, ll, cumsum):
    for i in range(n - ll + 1):
        if (cumsum[i + ll] - cumsum[i]) % m != 0:
            return False
    return True


def dfs(pos, arr, total, n, m, ll, ans, cumsum):
    if total >= ans:
        return ans

    if pos == n:
        cumsum[n] = (cumsum[n - 1] + arr[n - 1]) % m
        if check(arr, n, m, ll, cumsum):
            return min(ans, total)
        return ans

    if pos > 0:
        cumsum[pos] = (cumsum[pos - 1] + arr[pos - 1]) % m

    if pos >= ll and (cumsum[pos] - cumsum[pos - ll]) % m != 0:
        return ans

    orig = arr[pos]
    start = (m - (orig % m)) % m
    for i in range(m):
        inc = (i + start) % m
        arr[pos] = (orig + inc) % m
        ans = dfs(pos + 1, arr, total + inc, n, m, ll, ans, cumsum)
        if ans == 0:
            return 0
    arr[pos] = orig
    return ans


def solve(n, m, ll, a):
    cumsum = [0] * (n + 1)
    ans = dfs(0, a.copy(), 0, n, m, ll, float("inf"), cumsum)
    return ans if ans != float("inf") else -1


if __name__ == "__main__":
    n, m, ll = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, ll, a))
