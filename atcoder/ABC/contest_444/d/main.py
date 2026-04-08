def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    lists = [0] * (10**7)
    s_digit = 0
    target = 0
    for i in range(N):
        for j in range(s_digit, A[i]):
            pass
            # base = 10 ** j
            # target += (N - i) * base
            # digit = target % 10
            # lists.append(digit)
            # target -= digit * base
        s_digit = A[i]
    # reversed(lists)
    print(target)
    return


if __name__ == "__main__":
    main()
