def main():
    concat_strings = []
    N, K, X = map(int, input().split())
    strings = [input() for _ in range(N)]

    def create_patterns(n: int, k: int, pattern: tuple, depth: int):
        if depth == k:
            tmp_strs = []
            for p in pattern:
                tmp_strs.append(strings[p])
            concat_strings.append("".join(tmp_strs))
            return
        for i in range(n):
            tmp = pattern + (i,)
            create_patterns(n, k, tmp, depth + 1)

    create_patterns(N, K, (), 0)
    concat_strings.sort()
    print(concat_strings[X - 1])
    return


if __name__ == "__main__":
    main()
