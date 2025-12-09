from sortedcontainers import SortedList

def main():
    n, q = map(int, input().split())
    black_list = SortedList()
    element = 0
    white_count = n
    d = {}
    for _ in range(q):
        l, r = map(int, input().split())
        counter = r - l
        index = black_list.bisect_left(l)
        if element == index:
            black_list.add(l)
            element += 1
            white_count -= counter + 1
            d[l] = counter
        else:
            ll = []
            for i in range(index, element):
                print(white_count)
    return


if __name__ == "__main__":
    main()
