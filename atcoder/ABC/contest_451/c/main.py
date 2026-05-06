from bisect import bisect_right

import sortedcontainers


def main():
    result = []
    container = sortedcontainers.SortedList(result)
    Q = int(input())
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            container.add(query[1])
        else:
            index = bisect_right(container, query[1])
            while index:
                container.pop(0)
                index -= 1
        print(len(container))
    return


if __name__ == "__main__":
    main()
