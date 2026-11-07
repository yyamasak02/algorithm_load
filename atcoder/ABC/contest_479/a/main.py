def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = sum(A[i] for i in range(N) if i % 2 == 0)
    print(result)
    return


if __name__ == "__main__":
    main()
