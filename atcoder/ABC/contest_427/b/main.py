def main():
    n = int(input())
    a = [1, 1]
    for i in range(2, n + 1):
        list_i = list(map(int, list(str(a[-1]))))
        a.append(a[-1] + sum(list_i))
    print(a[n])
    return


if __name__ == "__main__":
    main()
