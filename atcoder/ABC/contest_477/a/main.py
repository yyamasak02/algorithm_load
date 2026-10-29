def main():
    order = "BYR"
    c = input()
    print(order[(order.index(c) + 1) % 3])
    return


if __name__ == "__main__":
    main()
