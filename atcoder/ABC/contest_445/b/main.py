def main():
    n = int(input())
    a = []
    length = 0
    for i in range(n):
        s = input()
        length = max(length, len(s))
        a.append(s)
    for c in a:
        c_len = len(c)
        dot_count = (length - c_len) // 2
        print(f"{"." * dot_count}{c}{"." * dot_count}")
    return


if __name__ == "__main__":
    main()
