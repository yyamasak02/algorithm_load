def main():
    N, W = map(int, input().split())
    foods = sorted(
        [tuple(map(int, input().split())) for _ in range(N)],
        key=lambda k: (-k[1], k[0]),
    )
    ans = [0]

    def on_off(index, value, weight):
        if index >= N:
            if weight <= W:
                ans.append(value)
            return
        if weight + foods[index][1] <= W:
            on_off(index + 1, value + foods[index][0], weight + foods[index][1])
        on_off(index + 1, value, weight)

    for i in range(N):
        # v, w = foods[i][0], foods[i][1]
        # if w >= W:
        #     continue
        on_off(i, 0, 0)
    # print(ans)
    print(max(ans))
    return


if __name__ == "__main__":
    main()
