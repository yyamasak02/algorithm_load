def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a not in d:
            d[a] = 0
        d[a] += 1
    max_number = max(d.values())
    print(sum(value in [max_number, max_number - 1] for key, value in d.items()))
    return


if __name__ == "__main__":
    main()
