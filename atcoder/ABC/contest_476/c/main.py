import sys


def main():
    input = sys.stdin.readline
    N: int = int(input())
    A: list[int] = list(map(int, input().split()))
    ordered_array: list[int, int] = sorted(
        [(A[i], i + 1) for i in range(N)], key=lambda x: x[0], reverse=True
    )
    result = [-1] * (N + 1)
    t1, t2, t3, nxt_idx = ordered_array[0], ordered_array[1], ordered_array[2], 3

    def progress(start, limit):
        while ordered_array[start][1] > limit:
            start += 1
        return start

    for i in range(N, 2, -1):
        if t1[1] > i:
            nxt_idx = progress(nxt_idx, i)
            t1 = ordered_array[nxt_idx]
            nxt_idx += 1
        if t2[1] > i:
            nxt_idx = progress(nxt_idx, i)
            t2 = ordered_array[nxt_idx]
            nxt_idx += 1
        if t3[1] > i:
            nxt_idx = progress(nxt_idx, i)
            t3 = ordered_array[nxt_idx]
            nxt_idx += 1
        # print(t1,t2,t3)
        result[i] = min(t1[0], t2[0], t3[0])
    result_str = "\n".join(map(str, result[3:]))
    print(result_str)
    return


if __name__ == "__main__":
    main()
