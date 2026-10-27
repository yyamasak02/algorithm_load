import sys


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    X, Y = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    result = [-1] * (M + 1)
    mod_bills, mod, total_buyable_drinks = Y, 0, 0
    for i in range(M):
        need_bills = ((B[i] - 1) // K) + 1
        if mod_bills < need_bills:
            break
        mod_bills -= need_bills
        mod += need_bills * K - B[i]
        total_buyable_drinks += 1
    result[total_buyable_drinks] = total_buyable_drinks
    mod = mod_bills * K + mod + X
    total_buyable_deserts = N
    for i in range(N):
        if mod < A[i]:
            total_buyable_deserts = i
            break
        mod -= A[i]
        result[total_buyable_drinks] += 1
    for i in reversed(range(total_buyable_drinks)):
        mod += B[i]
        counter = result[i + 1] - 1
        while total_buyable_deserts != N and mod >= A[total_buyable_deserts]:
            counter += 1
            mod -= A[total_buyable_deserts]
            total_buyable_deserts += 1
        result[i] = counter
    print(max(result))
    # print("[MAX] " , max(result), "\n[LOG] ", *result)
    return


if __name__ == "__main__":
    main()
