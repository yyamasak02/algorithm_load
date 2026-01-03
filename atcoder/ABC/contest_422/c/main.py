def main():
    t = int(input())
    for _ in range(t):
        na, nb, nc = map(int, input().split())
        x = min(na, nc, (na + nb + nc) // 3)
        print(x)
    return


if __name__ == "__main__":
    main()
