def main():
    N, M = map(int, input().split())
    result = "Yes" if (N + 1) // M >= 2 else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
