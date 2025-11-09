import sys
from bisect import bisect_left
from sortedcontainers import SortedList


def near_result(tmpList, length, index, y):
    result = 0
    # print("index, result, tmpList, y, length", index, result, tmpList, y, length)
    if index == length:
        prev = tmpList[index - 1]
        preprev = tmpList[index - 2]
        result += y - prev
        result -= prev - preprev
        result += min(prev - preprev, y - prev)
    else:
        x = index - 1
        z = index
        zv = tmpList[z]
        xv = tmpList[x]
        if x == 0:
            result -= zv - xv
            result += y - xv
        else:
            xxv = tmpList[x - 1]
            result -= min(zv - xv, xv - xxv)
            result += min(xv - xxv, y - xv)
        if z == length - 1:
            result -= zv - xv
            result += zv - y
        else:
            zzv = tmpList[z + 1]
            result -= min(zv - xv, zzv - zv)
            result += min(zv - y, zzv - zv)
        result += min(zv - y, y - xv)
    return result


input = sys.stdin.readline


def main():
    xSize: int = int(input())
    xList: list[int] = list(map(int, input().split()))

    # number, minNearIndex
    tmpList = SortedList()
    tmpList.add(0)
    tmpList.add(xList[0])
    result: int = 2 * xList[0]
    print(result)
    for elm_num, y in enumerate(xList[1::]):
        length: int = elm_num + 2
        index: int = bisect_left(tmpList, y)
        result += near_result(tmpList, length, index, y)
        # print(tmpList)
        print(result)
        tmpList.add(y)
    return


if __name__ == "__main__":
    main()
