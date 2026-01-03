def main():
    d, f = map(int, input().split())
    zan = d - f
    print(7 - (zan % 7))
    return


if __name__ == "__main__":
    main()
