def main():
    N, K, T = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    A.append(T)
    A.sort()
    result = ((A[0] - 1) // K) + 1 if A[0] != 0 else 0
    pre_start = (result - 1) * K if A[0] != 0 else 0
    for i in range(N + 1):
        A[i] = min(A[i], T)
        delta_time = A[i] - (pre_start + K)
        if delta_time > 0:
            result += ((delta_time - 1) // K) + 1
        # print(f"{i}番目: ({pre_start}, {A[i]})")
        pre_start = A[i]
        if A[i] >= T:
            break
    print(result)
    return


if __name__ == "__main__":
    main()
