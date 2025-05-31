if __name__ == "__main__":
    n: int = int(input())
    a: list[int] = list(map(int, input().split()))
    for i in range(n-1):
        if (a[i] >= a[i+1]):
            print("No")
            exit()
    print("Yes")