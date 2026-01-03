def main():
    s = input().split("-")
    i, j = int(s[0]), int(s[1])
    if j == 8:
        i = i + 1
        j = 1
    else:
        j += 1
    print(f"{i}-{j}")
    return


if __name__ == "__main__":
    main()
