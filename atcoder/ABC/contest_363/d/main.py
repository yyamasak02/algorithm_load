import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    count_by_digit = [0, 10]
    SIZE = 40
    for i in range(2, SIZE):
        half_width = i // 2
        result = 10**half_width - 10 ** (half_width - 1)
        if i % 2 == 1:
            count_by_digit.append(result * 10)
        else:
            count_by_digit.append(result)
    tmp = 0
    digit = 0
    for i in range(SIZE):
        if tmp + count_by_digit[i] >= n:
            digit = i
            break
        tmp += count_by_digit[i]
    result = ["0"] * digit
    rank = n - tmp
    half_digit = digit // 2
    for i in range(half_digit):
        if i == 0:
            num = (10 ** (half_digit - i)) * 1
        else:
            num = (10 ** (half_digit - i - 1)) * 1
        if half_digit % 2 == 0:
            div = rank // num
            mod = rank % num
            if i == 0:
                d = div + 1
            else:
                d = div
            result[i] = str(d)
            result[-i - 1] = str(d)
            rank -= num * div
        else:
            div = rank // num
            mod = rank % num
            if i == 0:
                d = div + 1
            else:
                d = div
            result[i] = str(d)
            result[-i - 1] = str(d)
            rank -= num * div
            if i == 0:
                tmp = 0
                for j in range(10):
                    if tmp + (num // 10) >= rank:
                        result[half_digit] = str(j)
                        break
                    tmp += num // 10
    print("".join(result))
    return


if __name__ == "__main__":
    main()
