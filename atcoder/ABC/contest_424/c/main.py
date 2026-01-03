from collections import deque


def main():
    n = int(input())
    skills = [False] * n
    visited = [False] * n
    d = {}
    target = deque()
    for i in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a == -1 and b == -1:
            target.append(i)
            continue
        if a not in d:
            d[a] = set()
        if b not in d:
            d[b] = set()
        d[a].add(i)
        d[b].add(i)
    while target:
        i = target.popleft()
        if visited[i] is True:
            continue
        visited[i] = True
        skills[i] = True
        if i not in d:
            continue
        for j in d[i]:
            if visited[j] is True:
                continue
            target.append(j)
    print(sum(skills))
    return


if __name__ == "__main__":
    main()
