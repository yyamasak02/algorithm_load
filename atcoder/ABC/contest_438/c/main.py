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
            if counter != 0:
                d.append((tmp, counter))
            tmp = a[i]
            counter = 0
        counter += 1
    counter %= 4
    if counter != 0:
        d.append((tmp, counter))
    already = deque()
    while d:
        pre_number, pre_counter = 0, 0
        if already:
            pre_number, pre_counter = already.pop()
        number, counter = d.popleft()
        if pre_number == number:
            pre_counter += counter
            pre_counter %= 4
            if pre_counter != 0:
                already.append((pre_number, pre_counter))
        else:
            already.append((pre_number, pre_counter))
            already.append((number, counter))
    result = 0
    for a, b in already:
        result += b
    print(result)
    return


if __name__ == "__main__":
    main()
