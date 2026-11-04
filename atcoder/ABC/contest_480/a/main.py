def main():
    S_1 = input()
    S_2 = input()
    a_pos = (1, S_1.index("A")) if S_1.count("A") != 0 else (2, S_2.index("A"))
    d_pos = (1, S_1.index("D")) if S_1.count("D") != 0 else (2, S_2.index("D"))
    result = "Yes" if a_pos[0] == d_pos[0] or a_pos[1] == d_pos[1] else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
