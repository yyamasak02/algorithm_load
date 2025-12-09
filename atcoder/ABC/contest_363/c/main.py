import sys
from more_itertools import distinct_permutations


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    s = input().rstrip()
    answers = 0
    for tmp in distinct_permutations(s, n):
        tmp = "".join(tmp)
        is_ok = True
        for i in range(n - k + 1):
            for j in range(k):
                if tmp[i + j] != tmp[i + k - j - 1]:
                    break
            else:
                break
        else:
            answers += 1
    print(answers)
    return


if __name__ == "__main__":
    main()
