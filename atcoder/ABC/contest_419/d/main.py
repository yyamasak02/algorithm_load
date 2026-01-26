def main():
    n, m = map(int, input().split())
    s = list(input())
    t = list(input())
    transfer_counts = [0] * (n + 1)
    for _ in range(m):
        li, ri = map(int, input().split())
        li -= 1
        ri -= 1
        transfer_counts[li] += 1
        transfer_counts[ri + 1] -= 1
    ans = []
    tmp = 0
    for i in range(n):
        tmp += transfer_counts[i]
        if tmp % 2 == 0:
            ans.append(s[i])
        else:
            ans.append(t[i])
    print("".join(ans))
    return


if __name__ == "__main__":
    main()
