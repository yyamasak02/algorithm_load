def main():
    n, k = map(int, input().split())
    nodes = [set() for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nodes[a].add(b)
        nodes[b].add(a)
    v = list(map(int, input().split()))
    v = set(x - 1 for x in v)
    nodes_len_list = [len(node) for node in nodes]
    target_bad_points = [i for i, d in enumerate(nodes_len_list) if d == 1]
    result = n
    for index in target_bad_points:
        if index in v:
            continue
        connect_node = nodes[index].pop()
        nodes[connect_node].discard(index)
        result -= 1
        if len(nodes[connect_node]) == 1:
            target_bad_points.append(connect_node)
    print(result)
    return


if __name__ == "__main__":
    main()
