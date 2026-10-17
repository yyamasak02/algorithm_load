import sys


def main():
    input = sys.stdin.readline
    S = "".join("A" if c == "A" else "." for c in input().strip())
    print(S)
    return


if __name__ == "__main__":
    main()
