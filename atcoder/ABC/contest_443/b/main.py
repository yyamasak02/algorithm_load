def main():
    N, K = map(int, input().split())
    tmp, cnt = N, 0
    while tmp < K:
        N += 1
        tmp += N
        cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    main()
