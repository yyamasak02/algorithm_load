def main():
    N, K, M = map(int, input().split())
    picked = set()
    all_items = []
    max_values_by_items = [(0, 0, 0)] * (N + 1)
    for i in range(N):
        C, V = map(int, input().split())
        if max_values_by_items[C][1] < V:
            max_values_by_items[C] = (C, V, i)
        all_items.append((C, V, i))
    max_values_by_items.sort(key=lambda x: x[1], reverse=True)
    all_items.sort(key=lambda x: x[1], reverse=True)
    result = 0
    # print(max_values_by_items)
    # print(all_items)
    for i in range(M):
        result += max_values_by_items[i][1]
        picked.add(max_values_by_items[i][2])
    mod = K - M
    tmp = 0
    # print(picked)
    while mod > 0:
        if all_items[tmp][2] in picked:
            tmp += 1
            continue
        result += all_items[tmp][1]
        mod -= 1
        tmp += 1
    print(result)
    return


if __name__ == "__main__":
    main()
