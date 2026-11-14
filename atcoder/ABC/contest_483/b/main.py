def main():
    N, Q = map(int, input().split())
    K = list(map(int, input().split()))
    numbers = [i + 1 for i in range(N)]
    for i in range(Q):
        Ki = K[i]
        for i in range((Ki - 1) // 2 + 1):
            numbers[i], numbers[Ki - 1 - i] = -numbers[Ki - 1 - i], -numbers[i]
    for number in numbers:
        print(number)
    return


if __name__ == "__main__":
    main()
