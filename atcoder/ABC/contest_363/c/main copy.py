import sys
from itertools import permutations


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    s = input().rstrip()
    str_permutations = set(permutations(s, n))
    answers = 0
    half_count = k // 2
    prefix = 0
    if k % 2 == 1:
        prefix = 1
    for tmp in str_permutations:
        is_ok = True
        for i in range(n - k + 1):
            if tmp[i : i + half_count] == tmp[i + half_count + prefix : i + k]:
                is_ok = False
                break
        if is_ok is True:
            answers += 1
    print(answers)
    return


if __name__ == "__main__":
    main()
