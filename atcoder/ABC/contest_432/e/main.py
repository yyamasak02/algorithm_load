MAX_ELEMENTS = (10**5) * 5 + 10


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    initial_v = [0] * MAX_ELEMENTS
    for c in a:
        initial_v[c] += 1
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            x, y = int(query[1]) - 1, int(query[2])
            a[x] = y
        else:
            l, r = int(query[1]), int(query[2])
            pass
    return


if __name__ == "__main__":
    main()
