def main():
    tiles = [["#"], ["###", "#.#", "###"]]
    for i in range(1, 6):
        tile_size = len(tiles[i])
        tmp = [""] * tile_size * 3
        for j in range(9):
            if j == 4:
                for k in range(tile_size):
                    target = (tile_size * (j // 3)) + k
                    tmp[target] = tmp[target] + ("." * tile_size)
                continue
            for k in range(tile_size):
                target = (tile_size * (j // 3)) + k
                tmp[target] = tmp[target] + tiles[i][k]
        tiles.append(tmp)
    N = int(input())
    for tile in tiles[N]:
        print("".join(tile))
    return


if __name__ == "__main__":
    main()
