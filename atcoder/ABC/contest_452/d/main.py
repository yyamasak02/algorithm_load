def main():
    S = input()
    T = input()
    counter_s, counter_t = {}, {}
    for c in T:
        if c not in counter_t:
            counter_t[c] = 0
        counter_t[c] += 1
    for c in S:
        if c not in counter_s:
            counter_s[c] = 0
        counter_s[c] += 1
    print(counter_s, counter_t)
    return


if __name__ == "__main__":
    main()
