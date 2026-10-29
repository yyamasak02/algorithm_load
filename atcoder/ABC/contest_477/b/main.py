def main():
    N, D = map(int, input().split())
    X = list(map(int, input().split()))
    result = []
    for i in range(N):
        is_ok = True
        for j in range(N):
            if i == j:
                continue
            if abs(X[i] - X[j]) < D:
                is_ok = False
                break
        if is_ok is True:
            result.append(i + 1)
    print(len(result))
    print(*result)
    return


if __name__ == "__main__":
    main()
