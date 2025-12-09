import sys


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, h = map(int, input().split())
        cur_low = h
        cur_upper = h
        is_ok = True
        cur_time = 0
        for i in range(n):
            t, l, u = map(int, input().split())
            if is_ok is False:
                continue
            dt = t - cur_time
            min_height_from_low = max(0, cur_low - dt)
            max_height_from_upper = cur_upper + dt
            if max_height_from_upper < l or min_height_from_low > u:
                is_ok = False
            cur_low = max(min_height_from_low, l)
            cur_upper = min(max_height_from_upper, u)
            cur_time = t
        if is_ok is True:
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
