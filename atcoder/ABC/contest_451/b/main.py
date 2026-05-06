def main():
    N, M = map(int, input().split())
    result = [0] * (M + 1)
    for _ in range(N):
        a, b = map(int, input().split())
        result[b] += 1
        result[a] -= 1
    for n in result[1::]:
        print(n)
    return


if __name__ == "__main__":
    main()
