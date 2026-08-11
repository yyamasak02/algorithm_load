def main():
    x, y = map(int, input().split())
    result = "Yes" if y * 16 == 9 * x else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
