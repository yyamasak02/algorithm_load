import heapq


def main():
    X = int(input())
    smaller_hq = []
    bigger_hq = []  # マイナスで格納して常に最大値を取り出す
    heapq.heappush(bigger_hq, -X)
    N = int(input())

    def add_heapq(x):
        if x <= -bigger_hq[0]:
            heapq.heappush(bigger_hq, -x)
        else:
            heapq.heappush(smaller_hq, x)
        if len(bigger_hq) < len(smaller_hq) + 1:
            heapq.heappush(bigger_hq, -heapq.heappop(smaller_hq))
        if len(bigger_hq) > len(smaller_hq) + 1:
            heapq.heappush(smaller_hq, -heapq.heappop(bigger_hq))

    for i in range(N):
        a, b = map(int, input().split())
        add_heapq(a)
        add_heapq(b)
        print(-bigger_hq[0])
    return


if __name__ == "__main__":
    main()
