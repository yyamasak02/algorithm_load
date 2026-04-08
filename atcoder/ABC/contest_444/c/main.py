def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    max_count = A.count(max(A))
    ans = set()

    if N == 1:
        print(A[0])
        exit(0)
    a = A[0]
    if A.count(a) == N:
        ans.add(a)
    # 半分ケース
    half = (N + 1) // 2
    d = 0 if N % 2 == 0 else 1
    ok, target = True, A[0] + A[-1 - d]
    for i in range(half):
        if A[i] + A[-(i + 1) - d] != target:
            ok = False
            break
    if ok is True:
        if N % 2 == 0:
            ans.add(target)
        elif target == A[-1]:
            ans.add(target)

    # それ以外
    if (N - max_count) % 2 == 0:
        target_num = (N - max_count) // 2
        d = max_count
        ok, target = True, A[-1]
        for i in range(target_num):
            if A[i] + A[-(i + 1) - d] != target:
                ok = False
                break
        if ok is True:
            ans.add(target)
    print(*sorted(list(ans)))
    # print(max_count)
    return


if __name__ == "__main__":
    main()
