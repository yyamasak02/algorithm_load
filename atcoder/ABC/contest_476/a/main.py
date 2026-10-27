def main():
    S = input()
    S = f"{S}r" if S[-1] == "e" else f"{S}er"
    print(S)
    return


if __name__ == "__main__":
    main()
