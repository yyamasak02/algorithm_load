def is_potentially_loop(tmp: str, k: int) -> tuple[bool, str]:
    half_len = k // 2
    tmp_list = list(tmp)
    for i in range(half_len):
        if tmp[half_len] != tmp[-half_len - 1]:
            if tmp[half_len] != "?" and tmp[-half_len - 1] != "?":
                return (False, "")
    for i in range(half_len):
        if tmp[half_len] != tmp[-half_len - 1]:
            if tmp[half_len] == "?":
                tmp_list[half_len] = tmp[-half_len - 1]
            elif tmp[-half_len - 1] == "?":
                tmp_list[-half_len - 1] = tmp[half_len]
            else:
                return (False, "")
    return (True, "".join(tmp_list))


def main():
    n, k = map(int, input().split())
    s = input()
    hits = {}
    for i in range(n - k):
        tmp = is_potentially_loop(s[i : i + k], k)
        if tmp[0] is True:
            if tmp not in hits:
                hits[tmp] = 0
            hits[tmp] += 1
    print(hits)
    return


if __name__ == "__main__":
    main()
