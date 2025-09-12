from multiprocessing import Pool


def calculate(args):
    na, nb, nc = args
    ans: int = 0
    min_v: int = min(na, nb, nc)
    ans += min_v
    na -= min_v
    nb -= min_v
    nc -= min_v
    min_v, max_v = min(na, nc), max(na, nc)
    if 2 * min_v < max_v:
        ans += min_v
    else:
        x = max_v - min_v
        ans += x
        min_v -= x
        max_v -= 2 * x
        counter = min_v // 3
        ans += counter * 2
        min_v %= 3
        if min_v == 2:
            ans += 1
    return ans


if __name__ == "__main__":
    t: int = int(input())
    inputs: list[tuple[int, int, int]] = [
        tuple(map(int, input().split())) for _ in range(t)
    ]

    with Pool() as pool:
        results = pool.map(calculate, inputs)

    print(*results, sep="\n")
