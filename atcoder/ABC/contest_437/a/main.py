def main():
    d = {}
    h, w, n = map(int, input().split())
    for i in range(h):
        a = list(map(int, input().split()))
        for j in range(w):
            d[a[j]] = i + 1
    result = [0] * (h + 1)
    for i in range(n):
        b = int(input())
        if b in d:
            result[d[b]] += 1
    print(max(result))
    return


if __name__ == "__main__":
    main()
