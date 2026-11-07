def main():
    _ = int(input())
    S = input().split("S")
    print(max(len(s) for s in S))
    return


if __name__ == "__main__":
    main()
