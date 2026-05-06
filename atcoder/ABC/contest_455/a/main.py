def main():
    a, b, c = map(int, input().split())
    result = "Yes" if a != b and b == c else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
