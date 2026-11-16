def main():
    S = input()
    d = {}
    for c in S:
        if c not in d:
            d[c] = 0
        d[c] += 1
    max_value = max(d.values())
    target_chars = "".join(key for key, value in d.items() if value == max_value)
    result = [c for c in S if c not in target_chars]
    print("".join(result))
    return


if __name__ == "__main__":
    main()
