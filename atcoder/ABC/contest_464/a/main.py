def main():
    S = input()
    size = len(S)
    west_size = S.count("W")
    result = "West" if west_size > size - west_size else "East"
    print(result)
    return


if __name__ == "__main__":
    main()
