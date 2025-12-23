def main():
    d = {"Ocelot": 0, "Serval": 1, "Lynx": 2}
    x, y = input().split()
    print("Yes" if d[x] >= d[y] else "No")
    return


if __name__ == "__main__":
    main()
