def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for l in range(n - 1):
        for r in range(l + 1, n):
            sum_a = sum(a[l : r + 1])
            is_ok = True
            for k in range(l, r + 1):
                if sum_a % a[k] == 0:
                    is_ok = False
                    break
            if is_ok is True:
                result += 1
    print(result)
    return


if __name__ == "__main__":
    main()
