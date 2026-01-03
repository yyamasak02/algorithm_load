from collections import deque


def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = deque()
    tmp = None
    counter = 0
    for i in range(n):
        if tmp is None:
            tmp = a[i]
        if tmp != a[i]:
            counter %= 4
            d.append((tmp, counter))
            tmp = a[i]
            counter = 0
        counter += 1
    counter %= 4
    d.append((tmp, counter))
    size = len(d)
    while True:
        already = deque()
        already_size = 0
        tmp_number, tmp_counter = d.popleft()
        while d:
            number, counter = d.popleft()
            if tmp_number == number:
                tmp_counter += counter
                tmp_counter %= 4
            else:
                tmp_counter %= 4
                if tmp_counter != 0:
                    already.append((tmp_number, tmp_counter))
                    already_size += 1
                tmp_number = number
                tmp_counter = counter
        tmp_counter %= 4
        if tmp_counter != 0:
            already.append((tmp_number, tmp_counter))
            already_size += 1
        if already_size >= size or already_size == 0:
            break
        d = already
        size = already_size
    result = 0
    for a, b in already:
        result += b
    print(result)
    return


if __name__ == "__main__":
    main()
