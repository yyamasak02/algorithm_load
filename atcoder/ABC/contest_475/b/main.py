def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = [0, 0, 0]
    for a in A:
        bill_count = a // 1000 if a % 1000 == 0 else a // 1000 + 1
        return_money = bill_count * 1000 - a
        tmp = return_money // 100
        return_money -= tmp * 100
        ans[2] += tmp
        tmp = return_money // 10
        return_money -= tmp * 10
        ans[1] += tmp
        ans[0] += return_money
    print(*ans)
    return


if __name__ == "__main__":
    main()
