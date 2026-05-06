def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    array_sum = sum(A)
    d = {}
    for n in A:
        if n not in d:
            d[n] = 0
        d[n] += n
    sum_of_each_number_list = sorted(d.values(), reverse=True)
    iter_num = min(len(sum_of_each_number_list), K)
    for i in range(iter_num):
        array_sum -= sum_of_each_number_list[i]
    print(array_sum)
    return


if __name__ == "__main__":
    main()
