def main():
    r: int = int(input())
    line_count = (r - 1) * 4 + 1
    tmp = 0
    r_2 = r**2
    for i in range(r - 1):
        yoko: float = 0.5 + (r - 1) - i
        m = int((r_2 - yoko**2) ** (1 / 2) - 0.5)
        tmp += m
    print(line_count + tmp * 4)
    return


if __name__ == "__main__":
    main()
