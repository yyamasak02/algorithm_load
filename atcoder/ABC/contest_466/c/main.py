def main():
    N = int(input())
    result = 0
    for i in range(1, N):
        left, right = i, N + 1
        while right - left > 1:
            mid = (left + right) // 2
            print(f"? {i} {mid}")
            ans = input()
            if ans == "Yes":
                left = mid
            else:
                right = mid
        result += left - i
    print(f"! {result}")
    return


if __name__ == "__main__":
    main()
