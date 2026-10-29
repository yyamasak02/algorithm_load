def main():
    N, V = map(int, input().split())
    W = list(map(int, input().split()))
    result = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i + j + 2 > V:
                break
            for k in range(N):
                if j == k or i == k:
                    continue
                if i + j + k + 3 > V:
                    break
                result = max(result, W[i] + W[j] + W[k])
    print(result)
    return


if __name__ == "__main__":
    main()
