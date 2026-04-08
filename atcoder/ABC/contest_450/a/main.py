def main():
    n = int(input())
    array = [str(i) for i in range(n, 0, -1)]
    print(",".join(array))
    return


if __name__ == "__main__":
    main()
