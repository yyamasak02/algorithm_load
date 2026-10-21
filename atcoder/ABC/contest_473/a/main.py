def main():
    N = int(input())
    A = list(map(int, input().split()))
    second_half_sum = sum(A[N // 2 : :])
    print(second_half_sum)
    return


if __name__ == "__main__":
    main()
