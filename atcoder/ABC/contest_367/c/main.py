def main():
    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    ll = set()
    result = []
    tmp = 50 // k
    for i in range(1, tmp + 1):
        ll.add(i * k)

    def runner(index: int, sum_v: int, value: int):
        if index >= n:
            if sum_v in ll:
                result.append(value)
            return
        for v in range(1, r[index] + 1):
            runner(index + 1, sum_v + v, (value * 10) + v)

    runner(0, 0, 0)
    result.sort()
    for e in result:
        print(" ".join(list(str(e))))
    return


if __name__ == "__main__":
    main()
