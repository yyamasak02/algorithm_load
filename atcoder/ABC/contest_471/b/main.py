def main():
    N: int = int(input())
    d: dict[str, int] = {}
    for _ in range(N):
        s = "".join(map(str.lower, input()))
        if s not in d:
            d[s] = 0
        d[s] += 1
    print(max(d.values()))
    return


if __name__ == "__main__":
    main()
