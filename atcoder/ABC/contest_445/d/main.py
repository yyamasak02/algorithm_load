def main():
    H, W, N = map(int, input().split())
    pieces = []
    placed = [False] * N
    positions = [None] * N
    for i in range(N):
        h, w = map(int, input().split())
        pieces.append((h, w, i))
    sorted_height = sorted(pieces, key=lambda x: -x[0])
    sorted_width = sorted(pieces, key=lambda x: -x[1])
    wi, hi = 0, 0
    sw, sh = 1, 1
    # print("height: ", sorted_height)
    # print("width: ", sorted_width)
    while hi < N or wi < N:
        if (
            hi < N
            and sorted_height[hi][0] == H - (sh - 1)
            and placed[sorted_height[hi][2]] == False
        ):
            piece = sorted_height[hi]
            placed[piece[2]] = True
            positions[piece[2]] = (sh, sw)
            sw += piece[1]
            hi += 1
        elif (
            wi < N
            and sorted_width[wi][1] == W - (sw - 1)
            and placed[sorted_width[wi][2]] == False
        ):
            piece = sorted_width[wi]
            placed[piece[2]] = True
            positions[piece[2]] = (sh, sw)
            sh += piece[0]
            wi += 1
        else:
            hi += 1
            wi += 1
        # The line `print("remain: ", H - sh + 1, W - sw + 1)` is calculating and printing the
        # remaining space available for placing pieces in the grid.
        # print("remain: ", H - sh + 1, W - sw + 1)
    for q in positions:
        print(q[0], q[1])
    return


if __name__ == "__main__":
    main()
