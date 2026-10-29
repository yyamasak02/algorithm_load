import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline
    Q = int(input())
    S = input().rstrip()
    T = input().rstrip()
    t_size = len(T)
    part_string_positions = []
    for i in range(len(S) - t_size + 1):
        is_ok = all(S[i + j] == T[j] for j in range(t_size))
        if is_ok:
            part_string_positions.append(i)
    # print(part_string_positions)
    out = []
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        l, r = (
            bisect_left(part_string_positions, L),
            bisect_right(part_string_positions, R - t_size + 1),
        )
        out.append("Yes" if r - l > 0 else "No")
    print("\n".join(out))
    return


if __name__ == "__main__":
    main()
