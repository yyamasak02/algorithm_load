import sys


def main():
    data = sys.stdin.buffer.read().split()
    N, Q = int(data[0]), int(data[1])
    is_tile_exists = [False] * (N + 1)
    is_color_determined = [False] * (N + 1)
    tile_color = ["a"] * (N + 1)
    queries = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(Q)]
    for query in queries:
        if query[0] == b"1":
            x = int(query[1])
            is_tile_exists[x] = not is_tile_exists[x]
    target = set([i + 1 for i in range(N) if is_tile_exists[i + 1] is False])
    for query in reversed(queries):
        if query[0] == b"1":
            x = int(query[1])
            is_tile_exists[x] = not is_tile_exists[x]
            if is_color_determined[x] is False:
                if is_tile_exists[x] is True:
                    target.discard(x)
                else:
                    target.add(x)
        else:
            for i in target:
                tile_color[i] = query[1].decode()
                is_color_determined[i] = True
            target = set()
    print("".join(tile_color[1:]))
    return


if __name__ == "__main__":
    main()
