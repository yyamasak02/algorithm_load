def main():
    _ = int(input())
    l_list = list(map(int, input().split()))
    ans, value, total = 10**9, 0, sum(l_list)
    for l in l_list:
        value += l
        ans = min(ans, abs(total - 2 * value))
    print(ans)
    return


if __name__ == "__main__":
    main()
