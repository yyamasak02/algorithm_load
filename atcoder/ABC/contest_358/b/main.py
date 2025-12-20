def main():
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    result = [t[0] + a]
    for i in range(1, n):
        result.append(max(t[i], result[-1]) + a)
    for res in result:
        print(res)
    return


if __name__ == "__main__":
    main()
