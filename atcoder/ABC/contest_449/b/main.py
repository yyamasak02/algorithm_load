def main():
    H, W, Q = map(int, input().split())
    fields = [[False] * W for _ in range(H)]
    h, w = H, W
    for _ in range(Q):
        sig, target = map(int, input().split())
        if sig == 1:
            print(w * target)
            h -= target
        else:
            print(h * target)
            w -= target
    return


if __name__ == "__main__":
    main()
