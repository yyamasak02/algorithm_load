if __name__ == "__main__":
    n, k = map(int, input().split())
    ans = [k]
    for _ in range(n):
        nxt = []
        for a in ans:
            nxt.append(a // 2)
            nxt.append(a - a // 2)
        ans = nxt
    print(max(ans) - min(ans))
    print(*ans)
