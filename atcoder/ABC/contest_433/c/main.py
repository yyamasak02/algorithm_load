def main2():
    s = list(map(int, list(input())))
    size = len(s)
    # print(s)
    result = 0
    number = s[0]
    left_size = 1
    right_size = 0
    for i in range(1, size):
        if number == s[i]:
            left_size += 1
        elif number == s[i] - 1:
            right_size += 1
        else:
            result += min(left_size, right_size)
            if s[i - 1] == s[i] - 1:
                left_size = right_size
                right_size = 1
                number = s[i - 1]
            else:
                left_size = 1
                right_size = 0
                number = s[i]
    result += min(left_size, right_size)
    print(result)

    return


def main():
    s = list(map(int, list(input())))
    size = len(s)
    # print(s)
    result = 0
    number = s[0]
    left_size = 1
    right_size = 0
    i = 1
    while i < size:
        if number == s[i]:
            i += 1
            left_size += 1
        elif number == s[i] - 1:
            right_size = 0
            while right_size < size - i:
                if number == s[i + right_size] - 1:
                    right_size += 1
                else:
                    break
            result += min(left_size, right_size)
            number = s[i + right_size - 1]
            left_size = right_size
            i += right_size
        else:
            number = s[i]
            left_size = 1
            i += 1
    print(result)

    return


if __name__ == "__main__":
    main()
