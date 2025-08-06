def ft_bisect_left(n, x, a) -> int:
    left = -1
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid
        else:
            left = mid
    return left


if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(ft_bisect_left(n, x, a) + 1)
