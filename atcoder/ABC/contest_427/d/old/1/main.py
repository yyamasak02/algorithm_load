import sys


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        s = input().strip()
        g = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split())
            g[u - 1].append(v - 1)

        win = [c == "A" for c in s]
        for step in range(2 * k):
            nxt = [False] * n
            turn_alice = (2 * k - 1 - step) % 2 == 0
            if turn_alice:
                for v in range(n):
                    for to in g[v]:
                        if win[to]:
                            nxt[v] = True
                            break
            else:
                for v in range(n):
                    for to in g[v]:
                        if not win[to]:
                            nxt[v] = False
                            break
                    else:
                        nxt[v] = True
            win = nxt

        print("Alice" if win[0] else "Bob")
    return


if __name__ == "__main__":
    main()
