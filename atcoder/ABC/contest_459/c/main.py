from bisect import bisect_left, bisect_right

from sortedcontainers import SortedList


def main():
    N, Q = map(int, input().split())
    spaces = [0] * N
    so = SortedList(spaces)
    erase_size = 0
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            size = spaces[x - 1]
            so.discard(size)
            so.add(size + 1)
            spaces[x - 1] += 1

            index = bisect_right(so, erase_size)
            if index == 0:
                erase_size += 1
        else:
            y = query[1]
            index = bisect_left(so, y + erase_size)
            print(N - index)
        # print(erase_size)
        # print(spaces)
        # print(so)
    return


if __name__ == "__main__":
    main()
