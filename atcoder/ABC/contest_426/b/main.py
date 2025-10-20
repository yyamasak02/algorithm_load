def main():
    s = list(input())
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    for key, v in d.items():
        if v == 1:
            print(key)
            break
    return


if __name__ == "__main__":
    main()
