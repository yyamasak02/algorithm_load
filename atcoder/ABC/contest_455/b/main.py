def main():
    H, W = map(int, input().split())
    fields = [input() for _ in range(H)]
    counter = 0

    def check(h1, h2, w1, w2) -> bool:
        for i in range(h1, h2 + 1):
            target_i = h1 + h2 - i
            if target_i < 0 or H - 1 < target_i:
                continue
            for j in range(w1, w2 + 1):
                target_j = w1 + w2 - j
                if target_j < 0 or W - 1 < target_j:
                    continue
                if fields[i][j] != fields[target_i][target_j]:
                    return False
        return True

    for h1 in range(H):
        for h2 in range(h1, H):
            for w1 in range(W):
                for w2 in range(w1, W):
                    if check(h1, h2, w1, w2) is True:
                        counter += 1
    print(counter)
    return


if __name__ == "__main__":
    main()
