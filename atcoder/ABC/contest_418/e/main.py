from typing import List, Tuple


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def count_same_pairs(pairs: List[Tuple[int, int]]) -> int:
    pairs.sort()
    result = 0
    idx = 0
    while idx < len(pairs):
        j = idx
        while j < len(pairs) and pairs[j] == pairs[idx]:
            j += 1
        length = j - idx
        result += (length * (length - 1)) // 2
        idx = j
    return result


if __name__ == "__main__":
    n: int = int(input())
    slopes: List[Tuple[int, int]] = []
    centers: List[Tuple[int, int]] = []
    points: List[Tuple[int, int]] = []
    ans: int = 0

    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                slopes.append((0, 1))
            elif dy == 0:
                slopes.append((1, 0))
            else:
                if dx < 0:
                    dx, dy = -dx, -dy
                g = gcd(abs(dx), abs(dy))
                slopes.append((dx // g, dy // g))
            centers.append((points[i][0] + points[j][0], points[i][1] + points[j][1]))
    ans = count_same_pairs(slopes) - count_same_pairs(centers)
    print(ans)
