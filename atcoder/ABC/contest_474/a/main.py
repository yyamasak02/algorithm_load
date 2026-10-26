def main():
    X = int(input())
    candidates = [1, 2, 3]
    for c in candidates:
        if c != X:
            print(c)
            break
    return


if __name__ == "__main__":
    main()
