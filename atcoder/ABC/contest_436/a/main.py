def main():
    n = int(input())
    a = input()
    ans = "o" * (n - len(a)) + a
    print(ans)
    return


if __name__ == "__main__":
    main()
