def main():
    n, m = map(int, input().split())
    s = set(list(input()))
    t = set(list(input()))
    q = int(input())
    for _ in range(q):
        w = list(input())
        aoki = True
        takahashi = True
        for c in w:
            if c not in s:
                takahashi = False
            if c not in t:
                aoki = False
        if takahashi == aoki:
            print("Unknown")
        elif takahashi is True:
            print("Takahashi")
        else:
            print("Aoki")
    return


if __name__ == "__main__":
    main()
