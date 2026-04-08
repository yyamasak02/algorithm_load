def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    number_with_ids = sorted([(i + 1, A[i]) for i in range(N)], key=lambda x: x[1])
    for _ in range(Q):
        K = int(input())
        B = set(map(int, input().split()))
        tmp = 0
        while True:
            if number_with_ids[tmp][0] not in B:
                print(number_with_ids[tmp][1])
                break
            tmp += 1
    return


if __name__ == "__main__":
    main()
