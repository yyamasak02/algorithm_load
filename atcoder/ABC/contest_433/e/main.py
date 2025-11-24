def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        x_list = list(map(int, input().split()))
        y_list = list(map(int, input().split()))
        result = [[0] * m for _ in range(n)]

        def solve() -> bool:
            target_list = [None] * ((m * n) + 1)
            for i in range(n):
                target_list[x_list[i]] = (-1, i)
            for i in range(m):
                if target_list[y_list[i]] is not None:
                    target_list[y_list[i]] = (i, target_list[y_list[i]][1])
                else:
                    target_list[y_list[i]] = (i, -1)
            determined_list = [False] * ((m * n) + 1)
            for i in range(m):
                for j in range(n):
                    if y_list[i] == x_list[j]:
                        v = y_list[i]
                        if determined_list[v] is True:
                            return False
                        result[j][i] = v
                        determined_list[v] = True
            for i in range(m):
                for j in range(n):
                    if result[j][i] != 0:
                        continue
                    max_value = min(y_list[i], x_list[j])
                    tmp = None
                    for k in range(max_value, 0, -1):
                        if determined_list[k] is False:
                            if (target_list[k] is None) or (
                                target_list[k][0] == i or target_list[k][1] == j
                            ):
                                tmp = k
                                break
                    if tmp == None:
                        return False
                    result[j][i] = tmp
                    determined_list[tmp] = True
            return True

        if solve() is True:
            print("Yes")
            for res in result:
                print(*res)
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
