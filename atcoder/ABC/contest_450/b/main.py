def main():
    N = int(input())
    array = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N - 1):
        tmp = list(map(int, input().split()))
        for j in range(N - i - 1):
            array[i + 1][i + 2 + j] = tmp[j]

    def find(start, end, v) -> bool:
        for mid in range(start + 1, end):
            if array[start][mid] + array[mid][end] < v:
                return True
        return False

    flag = False
    for start in range(N - 2):
        for end in range(start + 2, N):
            if find(start + 1, end + 1, array[start + 1][end + 1]) is True:
                flag = True
                break
    if flag is True:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
