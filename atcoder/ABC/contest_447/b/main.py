def main():
    d = {}
    s = input()
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    max_num = max(d.values())
    a = []
    for key, value in d.items():
        if value == max_num:
            a.append(key)
    result = []
    for c in s:
        if c not in a:
            result.append(c)
    print("".join(result))
    return


if __name__ == "__main__":
    main()
