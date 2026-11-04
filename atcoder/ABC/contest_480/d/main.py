from bisect import bisect_left
from itertools import accumulate


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # prefix[k] = A[0] + ... + A[k-1]
    prefix = [0, *accumulate(A)]
    # prefix_sum[k] = prefix[1] + ... + prefix[k]
    prefix_sum = [0, *accumulate(prefix[1:])]
    # block_end[k] = 1 + 2 + ... + k (position where the k-th block ends)
    block_end = [0, *accumulate(range(1, N + 1))]

    for _ in range(Q):
        L, R = map(int, input().split())
        left_block = bisect_left(block_end, L)
        right_block = bisect_left(block_end, R)

        # whole blocks left_block+1 .. right_block, plus the partial head of left_block
        result = prefix_sum[right_block] - prefix_sum[left_block]
        result += prefix[left_block] - prefix[L - block_end[left_block - 1] - 1]
        # remove the unused tail of right_block
        result -= prefix[right_block] - prefix[R - block_end[right_block - 1]]
        print(result)


if __name__ == "__main__":
    main()
