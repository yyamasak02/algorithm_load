def main():
    d = {"Ocelot": 1, "Serval": 2, "Lynx": 3}
    x, y = map(str, input().split())
    result = "Yes" if d[x] >= d[y] else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
