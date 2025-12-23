def main():
    s = list(input())
    len_s = len(s)
    s.pop(len_s // 2)
    print("".join(s))
    return


if __name__ == "__main__":
    main()
