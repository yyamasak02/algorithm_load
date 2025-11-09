from bisect import bisect_left, bisect_right
import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    xList = list(map(int, input().split()))
    pList = list(map(int, input().split()))
    unionList: list[tuple] = list(zip(xList, pList))
    unionList.sort(key=lambda x: x[0])
    colList: list[tuple] = [(0, 0)]
    for x, p in unionList:
        colList.append((x, colList[-1][1] + p))
    colList.pop(0)
    q = int(input())
    # print(colList)
    for _ in range(q):
        l, r = map(int, input().split())
        leftIndex = bisect_left(colList, l, key=lambda x: x[0])
        rightIndex = bisect_right(colList, r, key=lambda x: x[0])
        removeValue = colList[leftIndex - 1][1] if leftIndex > 0 else 0
        # print(leftIndex, rightIndex)
        if rightIndex != 0:
            result = colList[rightIndex - 1][1] - removeValue
        else:
            result = 0
        print(result)
    return


if __name__ == "__main__":
    main()
