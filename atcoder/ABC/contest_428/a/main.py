def main():
    s, a, b, x = map(int, input().split())
    c = x // (a + b)
    nokori = x - c * (a + b)
    ans = c * s * a + min(a, nokori) * s
    print(ans)
    return


if __name__ == "__main__":
    main()
