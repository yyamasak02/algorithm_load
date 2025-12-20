def main():
    n, m = map(int, input().split())
    shops: list[str] = [input() for _ in range(n)]
    d = [0] * m
    res = []

    def switch(depth: int, on_count: int):
        if depth == n:
            if all(d):
                res.append(on_count)
            return
        for i in range(m):
            if shops[depth][i] == "o":
                d[i] += 1
        switch(depth + 1, on_count + 1)
        for i in range(m):
            if shops[depth][i] == "o":
                d[i] -= 1
        switch(depth + 1, on_count)

    switch(0, 0)
    print(min(res))
    return


if __name__ == "__main__":
    main()
