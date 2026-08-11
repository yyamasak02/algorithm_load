def main():
    N, D = map(int, input().split())
    size = 10**6 + 2
    # size = 22
    # 増えた人数, 減った人数
    cols = [[0, 0] for _ in range(size)]
    for _ in range(N):
        s, t = map(int, input().split())
        cols[s][0] += 1
        cols[t][1] += 1
    result = 0
    todays_number = 0
    # print(cols)
    reduce_number_from_today_to_d = sum(cols[i][1] for i in range(D - 1))
    for start in range(size - D):
        todays_number += cols[start][0] - cols[start][1]
        reduce_number_from_today_to_d += cols[start + D - 1][1] - cols[start][1]
        # print(f"days: {start} {todays_number} {reduce_number_from_today_to_d}")
        v = max(0, todays_number - reduce_number_from_today_to_d)
        result += v * (v - 1) // 2
    print(result)
    return


if __name__ == "__main__":
    main()
