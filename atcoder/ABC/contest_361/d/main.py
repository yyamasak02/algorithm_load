from collections import deque


def main():
    n = int(input())
    s = input()
    t = input() + ".."
    d = {}
    dec: deque = deque()
    origin_s = s + ".."
    step = 0
    dec.append((origin_s, step, n))
    d[origin_s] = 0
    while dec:
        s, step, b_index = dec.popleft()
        for i in range(n + 1):
            if s[i] != "." and s[i + 1] != ".":
                s_list = list(s)
                a, b = s[i], s[i + 1]
                s_list[i], s_list[i + 1] = ".", "."
                s_list[b_index], s_list[b_index + 1] = a, b
                new_s = "".join(s_list)
                if new_s not in d:
                    d[new_s] = step + 1
                    dec.append((new_s, step + 1, i))
    if t in d:
        print(d[t])
    else:
        print(-1)
    return


if __name__ == "__main__":
    main()
