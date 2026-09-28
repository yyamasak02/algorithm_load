def main():
    N = int(input())
    ans = [0] * (N + 1)
    c_list = list(map(int, input().split()))
    for c in c_list:
        ans[c] += 1
    max_value = max(ans)
    print(N - max_value)
    return


if __name__ == "__main__":
    main()
