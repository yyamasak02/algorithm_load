def main():
    N = int(input())
    people = sorted(
        [tuple(map(int, input().split())) for _ in range(N)],
        key=lambda x: x[0],
        reverse=True,
    )
    Q = int(input())
    t_list = list(map(int, input().split()))
    pairs = sorted([(t_list[i], i, 0) for i in range(Q)], key=lambda x: x[0])
    progress = 0
    for i in range(Q):
        while people[progress][1] <= pairs[i][0]:
            progress += 1
        pairs[i] = (pairs[i][0], pairs[i][1], people[progress][0])
    pairs.sort(key=lambda x: x[1])
    for pair in pairs:
        print(pair[2])
    return


if __name__ == "__main__":
    main()
