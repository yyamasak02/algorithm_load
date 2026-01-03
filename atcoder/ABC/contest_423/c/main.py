from bisect import bisect_left


def main():
    n, r = map(int, input().split())
    ll = list(map(int, input().split()))
    open_list = []
    for i in range(n):
        if ll[i] == 0:
            open_list.append(i)
    if len(open_list) == 0:
        print(0)
        exit()
    # open prev = index
    # open next = index + 1
    open_index = bisect_left(open_list, r)
    if open_index == 0:
        roc, rcc = len(open_list), int(open_list[-1] - r + 1 - len(open_list))
        print(roc + 2 * rcc)
    elif open_index == len(open_list):
        loc, lcc = open_index, int(r - open_list[0] - open_index)
        print(loc + 2 * lcc)
    else:
        loc, lcc = open_index, int(r - open_list[0] - open_index)
        roc, rcc = (
            len(open_list) - loc,
            int(open_list[-1] - r + 1 - len(open_list) + loc),
        )
        print(loc + 2 * lcc + roc + 2 * rcc)
    return


if __name__ == "__main__":
    main()
