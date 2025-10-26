import sys
from typing import List, Tuple


def calc_loop(v: int, n: int) -> int:
    v += 1
    if v > n // 2:
        v = n - v
    return v


def get_swapped_value(x: int, y: int, n: int, v: int) -> Tuple[int, int]:
    x += 1
    y += 1
    for _ in range(v):
        x, y = n + 1 - y, x
    return (x - 1, y - 1)


def main() -> None:
    input = sys.stdin.readline
    n: int = int(input())
    a: List[str] = [input().strip() for _ in range(n)]
    b: List[List[str]] = [[""] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            loop_count: int = min(calc_loop(x, n), calc_loop(y, n))
            qx, qy = get_swapped_value(x, y, n, loop_count)
            b[y][x] = a[qy][qx]

    for i in range(n):
        print("".join(b[i]))


if __name__ == "__main__":
    main()
