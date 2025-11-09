import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    loads = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        loads[u].append((v, w))
        loads[v].append((u, -w))
    visited = [False] * (n)
    scores = [-1] * (n)

    for i in range(n):
        if visited[i] == True:
            continue
        st = [i]
        scores[i] = 0
        while st:
            u = st.pop()
            for v, w in loads[u]:
                if not visited[v]:
                    visited[v] = True
                    scores[v] = scores[u] + w
                    st.append(v)
    print(*scores)
    return


if __name__ == "__main__":
    main()
