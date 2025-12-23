def main():
    n, m = map(int, input().split())
    d = {i: set() for i in range(n)}
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        d[u].add(v)
    colors = [0] * n
    result = 10**9

    def calc_delete():
        delete_count = 0
        for key, values in d.items():
            for value in values:
                if colors[key] == colors[value]:
                    delete_count += 1
        return delete_count

    def pattern(depth: int):
        nonlocal result
        if depth == n:
            result = min(result, calc_delete())
            return
        colors[depth] = 0
        pattern(depth + 1)
        colors[depth] = 1
        pattern(depth + 1)

    pattern(0)
    print(result)
    return


if __name__ == "__main__":
    main()
