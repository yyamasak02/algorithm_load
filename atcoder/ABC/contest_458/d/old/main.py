from sortedcontainers import SortedList


def main():
    X = int(input())
    X = [X]
    N = int(input())
    container = SortedList(X)
    for i in range(N):
        a, b = map(int, input().split())
        container.add(a)
        container.add(b)
        index = 2 * (i + 1) // 2
        print(container[index])
    return


if __name__ == "__main__":
    main()
