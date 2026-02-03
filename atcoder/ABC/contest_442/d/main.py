def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    col = [0]
    for a in A:
        col.append(col[-1] + a)
    indexes = [i for i in range(N + 1)]
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 2:
            print(col[query[2]] - col[query[1] - 1])
        else:
            col[query[1]] = (
                col[query[1]] + A[indexes[query[1] + 1] - 1] - A[indexes[query[1]] - 1]
            )

            tmp = indexes[query[1]]
            indexes[query[1]] = indexes[query[1] + 1]
            indexes[query[1] + 1] = tmp
    return


if __name__ == "__main__":
    main()
