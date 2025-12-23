def ketawa(x: int) -> int:
    s = list(str(x))
    a = 0
    for c in s:
        a += int(c)
    return a


def main():
    a = [1, 1]
    for _ in range(100):
        a.append(a[-1] + ketawa(a[-1]))
    x = int(input())
    print(a[x])
    return


if __name__ == "__main__":
    main()
