def main():
    pair = [(0, 0)]
    dame_count = 0
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            if query[1] == "(":
                t = (pair[-1][0] + 1, pair[-1][1])
            else:
                t = (pair[-1][0], pair[-1][1] + 1)
            if t[0] < t[1]:
                dame_count += 1
            pair.append(t)
        else:
            t = pair.pop(-1)
            if t[0] < t[1]:
                dame_count -= 1

        if pair[-1][0] == pair[-1][1] and dame_count == 0:
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
