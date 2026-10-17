from sortedcontainers import SortedList


def main():
    _ = int(input())
    a_list = list(map(int, input().split()))
    s_list: SortedList = SortedList(a_list)
    dis, value = 0, 0
    index = s_list.bisect_left(0)
    while len(s_list) > 0:
        if index >= len(s_list):
            index = len(s_list) - 1
        elif abs(value - s_list[index - 1]) <= abs(value - s_list[index]):
            index = index - 1
        dis += abs(value - s_list[index])
        value = s_list[index]
        s_list.pop(index)
    print(dis)
    return


if __name__ == "__main__":
    main()
