def main():
    S = input()
    T = input()
    remove_s = S.replace("A", "")
    remove_t = T.replace("A", "")
    if remove_s != remove_t:
        print(-1)
        exit(0)

    def create_extract(target_str: str) -> list[int]:
        llist = []
        counter = 0
        size_s = len(target_str)
        for i in range(size_s):
            if target_str[i] == "A":
                counter += 1
            else:
                llist.append(counter)
                counter = 0
        llist.append(counter)
        return llist

    extract_s, extract_t = create_extract(S), create_extract(T)
    # print(extract_s, extract_t)
    result = 0
    size_s, size_t = len(extract_s), len(extract_t)
    max_len = max(size_s, size_t)
    for i in range(max_len):
        s_len = 0 if i >= size_s else extract_s[i]
        t_len = 0 if i >= size_t else extract_t[i]
        result += abs(s_len - t_len)
    print(result)
    return


if __name__ == "__main__":
    main()
