def main():
    result = 0
    n, k = map(int, input().split())
    for c in range(1, n + 1):
        digit_sum = sum(list(map(int, list(str(c)))))
        if digit_sum == k:
            result += 1
    print(result)
    return


if __name__ == "__main__":
    main()
