def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ca = [0]
    for c in a:
        ca.append(ca[-1] + c)
    for c in a:
        ca.append(ca[-1] + c)
    prefix = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            prefix += query[1]
            prefix %= n
        else:
            left = query[1]
            right = query[2]
            tr = prefix + right
            tl = prefix + left - 1
            print(ca[tr] - ca[tl])
    return


if __name__ == "__main__":
    main()
