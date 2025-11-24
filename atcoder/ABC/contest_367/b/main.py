def main():
    v, s = input().split(".")
    s = list(s)
    if s[-1] == "0":
        s.pop(-1)
    if s[-1] == "0":
        s.pop(-1)
    if s[-1] == "0":
        s.pop(-1)
    if len(s) == 0:
        print(v)
    else:
        print(f"{v}.{''.join(s)}")
    return


if __name__ == "__main__":
    main()
