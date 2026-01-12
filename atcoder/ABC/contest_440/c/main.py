def main():
    T = int(input())
    for _ in range(T):
        N, W = map(int, input().split())
        c_list = list(map(int, input().split()))
        ans = 0
        target_list = [0] * (2 * W)
        for i in range(N):
            v = i + 1
            target_list[v % (2 * W)] += c_list[i]
            if (v % (2 * W)) < W:
                ans += c_list[i]
        prev = ans
        for i in range(2 * W):
            minus = (W - 1 - i) % (2 * W)
            plus = ((2 * W) - 1 - i) % (2 * W)
            prev -= target_list[minus]
            prev += target_list[plus]
            ans = min(ans, prev)
        print(ans)
    return


if __name__ == "__main__":
    main()
