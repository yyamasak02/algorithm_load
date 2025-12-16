def main():
    n = int(input())
    array = [[None] * (n + 1) for _ in range(n + 1)]
    array[0][(n - 1) // 2] = 1
    prev = (0, (n - 1) // 2)
    pre_num = 1
    for _ in range((n**2) - 1):
        new_r = (prev[0] - 1) % n
        new_c = (prev[1] + 1) % n
        new_v = pre_num + 1
        if array[new_r][new_c] is None:
            array[new_r][new_c] = new_v
            prev = (new_r, new_c)
            pre_num = new_v
        else:
            new_r = (prev[0] + 1) % n
            new_c = prev[1]
            array[new_r][new_c] = new_v
            prev = (new_r, new_c)
            pre_num = new_v
    for i in range(n):
        print(*array[i][:-1])
    return


if __name__ == "__main__":
    main()
