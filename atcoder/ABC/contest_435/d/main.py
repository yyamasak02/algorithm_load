from collections import deque


def main():
    n, m = map(int, input().split())
    fromKeyToValue = [[] for _ in range(n)]
    toKeyFromValue = [[] for _ in range(n)]
    hasBlacks = [False] * n
    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        fromKeyToValue[x].append(y)
        toKeyFromValue[y].append(x)
    q = int(input())
    for _ in range(q):
        p, v = map(int, input().split())
        v -= 1
        if p == 2:
            if hasBlacks[v] is True:
                print("Yes")
            else:
                print("No")
        else:
            if hasBlacks[v] is False:
                hasBlacks[v] = True
                queue: deque = deque()
                queue.append(v)
                while queue:
                    tmp = queue.popleft()
                    for fromValue in toKeyFromValue[tmp]:
                        if hasBlacks[fromValue] is False:
                            hasBlacks[fromValue] = True
                            queue.append(fromValue)
    return


if __name__ == "__main__":
    main()
