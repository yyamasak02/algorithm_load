def main():
    H, W = map(int, input().split())
    fields = [input() for _ in range(H)]
    while fields and all(c == "." for c in fields[0]):
        fields.pop(0)
    while fields and all(c == "." for c in fields[-1]):
        fields.pop(-1)
    # print(fields)
    while fields and all(fields[i][0] == "." for i in range(len(fields))):
        fields = [field[1::] for field in fields]
        # print(fields)
    while fields and all(fields[i][-1] == "." for i in range(len(fields))):
        fields = [field[:-1] for field in fields]
    for c in fields:
        print(c)
    return


if __name__ == "__main__":
    main()
