def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    counter = 10**9
    for i in range(n - m + 1):
        target_s = s[i : i + m]
        tmp = 0
        for j in range(m):
            if target_s[j] != t[j]:
                t1 = int(target_s[j])
                t2 = int(t[j])
                if t1 > t2:
                    tmp += t1 - t2
                else:
                    tmp += 10 - (t2 - t1)
        counter = min(counter, tmp)
    print(counter)
    return


if __name__ == "__main__":
    main()
