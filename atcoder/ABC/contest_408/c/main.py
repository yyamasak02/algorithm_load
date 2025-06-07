if __name__ == "__main__":
    n,m = map(int, input().split())
    walls = [0] * (n+2)
    for i in range(m):
        l,r = map(int, input().split())
        walls[l] += 1
        walls[r+1] -= 1
    ans = m+1
    tmp = 0
    for i in range(1, n+1):
        tmp += walls[i]
        ans = min(ans, tmp)
    print(ans)