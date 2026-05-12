if __name__ == "__main__":
    n, m = map(int, input().split())
    array = []
    for _ in range(m):
        a, b = map(int, input().split())
        array.append((a, b, a - b))
    array = sorted(array, key=lambda x: (x[2], x[0]))
    bottle: int = n
    empty: int = 0
    seals: int = 0
    empty = bottle
    bottle = 0
    for a, b, diff in array:
        if empty == 0:
            break
        if empty < a:
            continue
        res = ((empty - a) // diff) + 1
        empty -= diff * res
        # print(res)
        seals += res
    print(seals)
