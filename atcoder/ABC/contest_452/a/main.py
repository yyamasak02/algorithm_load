def main():
    p = [(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)]
    m, d = map(int, input().split())
    result = "Yes" if (m, d) in p else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
