


def solve(p_t) -> int:
    if not p_t:
        return 0
    return 


if __name__ == "__main__":
    ct = [0] * (10**2 + 1)
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        ct[i] += 1

    for i in range(d):
        ans += solve(ct[i::d])
        print(ct[i::d])