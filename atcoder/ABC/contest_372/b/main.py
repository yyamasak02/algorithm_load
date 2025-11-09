def main():
    m = int(input())
    a = []
    while True:
        three_count = 0
        tmp = 1
        while True:
            if tmp * 3 > m:
                break
            tmp *= 3
            three_count += 1
        m -= tmp
        a.append(three_count)
        if m == 0:
            break
    print(len(a))
    print(*a)

    # print(three_count)
    return


if __name__ == "__main__":
    main()
