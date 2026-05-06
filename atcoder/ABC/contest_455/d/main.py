def main():
    N, Q = map(int, input().split())
    places = [i for i in range(N)]
    parent = [-1] * N
    child = [-1] * N

    def find(c):
        tmp = c
        while parent[tmp] != -1:
            tmp = parent[tmp]
        return tmp

    for i in range(Q):
        c, p = map(int, input().split())
        c -= 1
        p -= 1
        # Cがいる場所の先頭要素を取得
        parent_node = find(c)
        # 元々cがいた場所は、その子要素が先頭になるためそうなるように更新
        if child[c] != -1:
            parent[child[c]] = -1
        # 移動先のpの親要素をcにする, 逆も更新
        parent[p] = c
        child[c] = p
        # parent要素の場所を更新する
        places[parent_node] = places[p]
        # print(places)
        # print(parent)
        # print(child)
        # print("--------------------")
    visited = [False] * N
    result = [0] * N
    head = [i for i in range(N) if parent[i] == -1]
    # print(head)
    for elm in head:
        place_index = places[elm]
        tmp = elm
        counter = 1
        while child[tmp] != -1:
            tmp = child[tmp]
            counter += 1
        result[place_index] += counter
    print(*result)
    return


if __name__ == "__main__":
    main()
