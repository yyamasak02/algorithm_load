def main():
    _ = int(input())
    X = list(map(int, input().split()))
    max_x = max(X)
    result = "Yes" if max_x < 0 else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
