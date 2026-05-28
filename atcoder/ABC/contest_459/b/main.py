def main():
    target = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    N = int(input())
    S = list(map(str, input().split()))
    ans = []
    for s in S:
        ll = 0
        for i in range(8):
            if s[0] in target[i]:
                ll = i + 2
                break
        ans.append(str(ll))
    print("".join(ans))
    return


if __name__ == "__main__":
    main()
