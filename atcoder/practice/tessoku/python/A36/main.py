def main():
    n, k = map(int, input().split())
    minimum_num: int = (n - 1) * 2
    if k >= minimum_num and k % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
