def main():
    s = list(input())
    s_len = len(s)
    s.pop(s_len // 2)
    print("".join(s))
    return


if __name__ == "__main__":
    main()
