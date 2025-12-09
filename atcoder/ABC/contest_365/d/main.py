def main():
    n = int(input())
    hands = list(input())
    dp = [None] * (n + 1)
    dp[0] = {"R": 0, "S": 0, "P": 0}
    paper = 0
    rock = 0
    sci = 0
    for i in range(1, n + 1):
        if hands[i - 1] == "R":
            paper = 1
            rock = 0
            sci = -(10**9)
        elif hands[i - 1] == "S":
            rock = 1
            sci = 0
            paper = -(10**9)
        elif hands[i - 1] == "P":
            sci = 1
            paper = 0
            rock = -(10**9)
        dp[i] = {
            "R": max(dp[i - 1]["S"], dp[i - 1]["P"]) + rock,
            "S": max(dp[i - 1]["R"], dp[i - 1]["P"]) + sci,
            "P": max(dp[i - 1]["R"], dp[i - 1]["S"]) + paper,
        }
    print(max(dp[-1].values()))
    return


if __name__ == "__main__":
    main()
