def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    left, right = 1, A[1] + K + 1

    def isok(x):
        # ans を x 以上にすることができますか？
        nk = 0
        for i in range(1, N + 1):
            if A[i] < x:
                nk += (x - A[i] + i - 1) // i
                if nk > K:
                    return False
        return True

    while right - left > 1:
        mid = (right + left) // 2
        if isok(mid):
            left = mid
        else:
            right = mid
    print(left)
    return


if __name__ == "__main__":
    main()
