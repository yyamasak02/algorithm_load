def main():
    s = input()
    result = "Yes" if s[0] == s[1] and s[1] == s[2] else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
