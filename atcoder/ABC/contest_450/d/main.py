def main():
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(N):
        array[i] = array[i] % K
    array.sort()
    min_diff = 10**9
    for i in range(N - 1):
        min_diff = min(min_diff, array[i] + K - array[i + 1])
    min_diff = min(min_diff, abs(array[-1] - array[0]))
    print(min_diff)
    return


if __name__ == "__main__":
    main()
