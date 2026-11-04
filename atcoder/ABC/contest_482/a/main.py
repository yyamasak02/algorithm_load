def main():
    S = input()
    o_count = S.count("o")
    if o_count % 2 == 0:
        print("even")
    else:
        print("odd")
    return


if __name__ == "__main__":
    main()
