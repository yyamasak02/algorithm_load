from bisect import bisect_left, bisect_right


def main():
    N, L, R = map(int, input().split())
    S = input()
    d = {}
    for index, c in enumerate(S):
        if c not in d:
            d[c] = []
        d[c].append(index)
    result = 0
    for array in d.values():
        size = len(array)
        for index in range(size - 1):
            i = array[index]
            min_j = bisect_left(array, i + L, index + 1)
            max_j = bisect_right(array, i + R, index + 1)
            # print(min_j, max_j, array)
            if min_j == size:
                continue
            result += max_j - min_j
    print(result)
    return


if __name__ == "__main__":
    main()
