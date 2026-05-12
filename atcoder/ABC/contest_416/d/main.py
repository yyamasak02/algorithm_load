def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = sorted([i % M for i in list(map(int, input().split()))], reverse=True)
        B = sorted([i % M for i in list(map(int, input().split()))], reverse=False)
        result = sum((A[i] + B[i]) % M for i in range(N))
        print(result)
    return


if __name__ == "__main__":
    main()
