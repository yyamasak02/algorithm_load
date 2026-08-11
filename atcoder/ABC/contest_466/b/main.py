def main():
    N, M = map(int, input().split())
    values = [-1] * (M + 1)
    for _ in range(N):
        C, S = map(int, input().split())
        values[C] = max(values[C], S)
    print(*values[1::])
    return


if __name__ == "__main__":
    main()
