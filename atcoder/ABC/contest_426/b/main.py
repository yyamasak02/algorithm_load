def main():
    d = {}
    s = input()
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    for key, value in d.items():
        if value == 1:
            print(key)
            break
    return


if __name__ == "__main__":
    main()
