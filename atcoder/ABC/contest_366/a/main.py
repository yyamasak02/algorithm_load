def main():
    n, t, a = map(int, input().split())
    result = "Yes" if t >= (n // 2) + 1 or a >= (n // 2) + 1 else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
