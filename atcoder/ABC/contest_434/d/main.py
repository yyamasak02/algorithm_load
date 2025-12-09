import sys


def main():
    input = sys.stdin.readline
    FIELD_NUM = 2000
    fields = [[0] * (FIELD_NUM + 1) for _ in range((FIELD_NUM + 1))]
    clouds = [[0] * (FIELD_NUM + 1) for _ in range((FIELD_NUM + 1))]
    n = int(input())
    exclusive = [0] * n

    for i in range(n):
        u, d, l, r = map(int, input().split())
        u, d, l, r = u - 1, d - 1, l - 1, r - 1
        fields[u][l] += 1
        fields[u][r + 1] -= 1
        fields[d + 1][l] -= 1
        fields[d + 1][r + 1] += 1
        clouds[u][l] += i
        clouds[u][r + 1] -= i
        clouds[d + 1][l] -= i
        clouds[d + 1][r + 1] += i

    for r in range(FIELD_NUM):
        for c in range(1, FIELD_NUM):
            fields[r][c] += fields[r][c - 1]
            clouds[r][c] += clouds[r][c - 1]
    for c in range(FIELD_NUM):
        for r in range(1, FIELD_NUM):
            fields[r][c] += fields[r - 1][c]
            clouds[r][c] += clouds[r - 1][c]

    non_cover_count = 0
    for r in range(FIELD_NUM):
        for c in range(FIELD_NUM):
            if fields[r][c] == 0:
                non_cover_count += 1
            elif fields[r][c] == 1:
                exclusive[clouds[r][c]] += 1
    for num in exclusive:
        print(num + non_cover_count)
    # print(rows)
    return


if __name__ == "__main__":
    main()
