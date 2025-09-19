if __name__ == "__main__":
    # 上、右、下、左
    edges: list[tuple] = [1000, 0, 0, 1000]
    h, w = map(int, input().split())
    fields: list[str] = []
    for i in range(h):
        s = input()
        fields.append(s)
        for j in range(w):
            if s[j] == "#":
                edges[0] = min(edges[0], i)
                edges[1] = max(edges[1], j)
                edges[2] = max(edges[2], i)
                edges[3] = min(edges[3], j)
    ok_flg: bool = True
    for i in range(edges[0], edges[2] + 1):
        for j in range(edges[3], edges[1] + 1):
            if fields[i][j] == ".":
                ok_flg = False
                break
        if ok_flg is not True:
            break
    if ok_flg is True:
        print("Yes")
    else:
        print("No")
