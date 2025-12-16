from sortedcontainers import SortedList


def main():
    n, q = map(int, input().split())
    black_list = SortedList()
    element = 0
    white_count = n
    d = {}
    for _ in range(q):
        ll, r = map(int, input().split())
        counter = r - ll
        index = black_list.bisect_left(ll)
        if element == index:
            black_list.add(ll)
            element += 1
            white_count -= counter + 1
            d[ll] = counter
        else:
            for i in range(index, element):
                print(white_count)
    return


if __name__ == "__main__":
    main()
