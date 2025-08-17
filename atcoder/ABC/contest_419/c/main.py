from dataclasses import dataclass
import math


@dataclass
class RCPair:
    r_min: int
    c_min: int
    r_max: int
    c_max: int


if __name__ == "__main__":
    n: int = int(input())
    rc: RCPair = RCPair(10**9, 10**9, 0, 0)
    for i in range(n):
        r, c = map(int, input().split())
        rc.r_min = min(rc.r_min, r)
        rc.r_max = max(rc.r_max, r)
        rc.c_min = min(rc.c_min, c)
        rc.c_max = max(rc.c_max, c)
    r_v: int = math.ceil((rc.r_max - rc.r_min) / 2)
    c_v: int = math.ceil((rc.c_max - rc.c_min) / 2)
    # print(r_v, c_v)
    print(max(r_v, c_v))
