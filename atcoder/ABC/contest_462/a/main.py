def main():
    match = "0123456789"
    s = input()
    res = []
    for c in s:
        if c in match:
            res.append(c)
    print("".join(res))
    return


if __name__ == "__main__":
    main()
