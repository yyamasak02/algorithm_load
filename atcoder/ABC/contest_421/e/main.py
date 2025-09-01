from itertools import product
from functools import cache
from collections import defaultdict
from fractions import Fraction as F


@cache
def calculate_expected(rest_turn: int, keep_idxs: tuple, a: tuple[int]):
    if len(keep_idxs) == 5:
        count: dict = defaultdict(int)
        for idx in keep_idxs:
            count[a[idx]] += 1
        return max(k * v for k, v in count.items())
    rest_dice: int = 5 - len(keep_idxs)
    ans: int = 0
    for deme_idxs in product(range(6), repeat=rest_dice):
        prob: F = F(1, 6**rest_dice)
        M: int = 0
        for keep in range(1 << rest_dice) if rest_turn != 1 else [(1 << rest_dice) - 1]:
            M = max(
                M,
                calculate_expected(
                    rest_turn - 1,
                    tuple(
                        sorted(
                            keep_idxs
                            + tuple(
                                idx
                                for i, idx in enumerate(deme_idxs)
                                if (keep >> i) & 1
                            )
                        )
                    ),
                    a,
                ),
            )
        ans += M * prob
    return ans


def create_prob_distribution() -> list[dict[tuple, F]]:
    deme_list: list[dict[tuple, F]] = [defaultdict(lambda: F(0, 1)) for _ in range(6)]
    for n in range(1, 6):
        posibble_way_num = 6**n
        for idxs in product(range(6), repeat=n):
            deme_list[n][tuple(sorted(idxs))] += F(1, posibble_way_num)
    return deme_list


def main():
    a = tuple(map(int, input().split()))
    deme_list: list[dict[tuple, F]] = create_prob_distribution()
    print(f"{float(calculate_expected(3, tuple(), a)):.10f}")


if __name__ == "__main__":
    main()
