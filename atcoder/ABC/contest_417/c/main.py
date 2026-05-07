from bisect import bisect_right


def main():
    # j - i = Ai + Aj
    # j - Aj = Ai + i
    N = int(input())
    A = list(map(int, input().split()))
    # I = [i + 1 + A[i] for i in range(N)]
    J = {}
    for j in range(N):
        key = (j + 1) - A[j]
        if key not in J:
            J[key] = []
        J[key].append(j + 1)
    result = 0
    for i in range(N):
        target = i + 1 + A[i]
        index = i + 1
        if target not in J:
            continue
        insert_position = bisect_right(J[target], index)
        size = len(J[target])
        result += size - insert_position
        # print(size - insert_position)
    print(result)
    # print(J)
    return


if __name__ == "__main__":
    main()
