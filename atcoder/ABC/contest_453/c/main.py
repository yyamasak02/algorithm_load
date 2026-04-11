def main():
    N = int(input())
    L = list(map(int, input().split()))
    d = {}
    d[0.5] = 0
    for i in range(N):
        keys = list(d.keys())
        tmp = {}
        for key in keys:
            counter = d[key]
            add_plus, add_menus = False, False
            plus, menus = key + L[i], key - L[i]
            if key < 0 and plus > 0:
                add_plus = True
            if key > 0 and menus < 0:
                add_menus = True
            if plus not in tmp:
                tmp[plus] = 0
            if menus not in tmp:
                tmp[menus] = 0
            max_plus = d[plus] if plus in d else 0
            max_menus = d[menus] if menus in d else 0
            tmp[plus] = max(tmp[plus], max_plus, counter + add_plus)
            tmp[menus] = max(tmp[menus], max_menus, counter + add_menus)
        d = tmp
    # print(d)
    print(max(d.values()))
    return


if __name__ == "__main__":
    main()
