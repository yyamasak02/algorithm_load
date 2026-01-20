def main():
    n = int(input())
    s = list(input())
    ac, bc = 0, 0
    for c in s:
        if c == "A":
            ac += 1
        if c == "B":
            bc += 1
    return


if __name__ == "__main__":
    main()
