def main():
    T = int(input())
    for _ in range(T):
        text = list(input())
        d = {}
        for char in text:
            if char not in d:
                d[char] = 0
            d[char] += 1
        size = len(text)
        max_count = max(d.values())
        if size % 2 == 0 and size // 2 < max_count:
            print("No")
            continue
        if size % 2 == 1 and (size // 2) + 1 < max_count:
            print("No")
            continue
        target = [""] * size
        value_to_strs = {}
        for key, value in d.items():
            if value not in value_to_strs:
                value_to_strs[value] = []
            value_to_strs[value].append(key)
        keys = sorted(value_to_strs.keys(), reverse=True)
        index = 1
        for key in keys:
            for char in value_to_strs[key]:
                for i in range(key):
                    target[index - 1] = char
                    index += 2
                    if index > size:
                        index = 2
        print("Yes")
        print("".join(target))
    return


if __name__ == "__main__":
    main()
