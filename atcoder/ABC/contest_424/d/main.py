def main():
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        ll = [list(input().rstrip()) for _ in range(h)]
        dirs = [(0, 0), (0, 1), (1, 0), (1, 1)]

        def is_target(i, j):
            if i >= h - 1 or i < 0:
                return False
            if j >= w - 1 or j < 0:
                return False
            return True

        def is_filled(i, j):
            for dy, dx in dirs:
                if ll[i + dy][j + dx] == ".":
                    return False
            return True

        target = []
        for i in range(h):
            for j in range(w):
                if is_target(i, j) is False:
                    continue
                if is_filled(i, j) is True:
                    target.append((i, j))
        if len(target) == 0:
            print(0)
            continue
        d = {}
        for index, q in enumerate(target):
            i = q[0]
            j = q[1]
            for dy, dx in dirs:
                if (i + dy, j + dx) not in d:
                    d[(i + dy, j + dx)] = set()
                d[(i + dy, j + dx)].add(index)
        filled_list = list(d.values())
        bit_size = len(target)
        dp = [[10**9] * 2**bit_size for _ in range(len(filled_list) + 1)]
        filled_indexes_set = set([0])
        dp[0][0] = 0
        for i in range(1, len(filled_list) + 1):
            target_set = filled_list[i - 1]
            number = 0
            for num in target_set:
                number += 2**num
            # print(target_set)
            # print(number)
            tmp_set = set()
            for index in filled_indexes_set:
                new_mask = index | number
                # print("after: ", number)
                dp[i][index] = min(dp[i - 1][index], dp[i][index])
                dp[i][new_mask] = min(dp[i - 1][index] + 1, dp[i][new_mask])
                tmp_set.add(index)
                tmp_set.add(new_mask)
            filled_indexes_set |= tmp_set
        print(dp[-1][-1])
        # pprint(d)
        # pprint(ll)
        # pprint(target)
    return


if __name__ == "__main__":
    main()
