def isPrime(x: int) -> bool:
    root_x: int = int(x ** (1 / 2))
    # print(root_x)
    for i in range(2, root_x + 1):
        if x % i == 0:
            return False
    return True


def main():
    q: int = int(input())
    for _ in range(q):
        print("Yes" if isPrime(int(input())) is True else "No")


if __name__ == "__main__":
    main()
