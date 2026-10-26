import math
from itertools import permutations


def main():
    S = input()
    size = len(S)
    d = {}

    def eratosthenes(sieve, n):
        if sieve[n] is False:
            return sieve
        for i in range(int(math.sqrt(n)) + 1):
            if i < 2:
                sieve[i] = False
            elif sieve[i]:
                for j in range(2, n // i + 1):
                    sieve[i * j] = False
        return sieve

    for i in range(size):
        if S[i] not in d:
            d[S[i]] = []
        d[S[i]].append(i)

    order = [-1] * size
    counter = 0
    for i in range(size):
        if order[i] != -1:
            continue
        for index in d[S[i]]:
            if order[index] != -1:
                continue
            order[index] = counter
        counter += 1
    # print(order)
    kinds_count = len(d.keys())
    counter = 0
    reversed_perms_list = list(reversed(list(permutations(range(10), kinds_count))))

    first = 0
    for i in order:
        first *= 10
        first += reversed_perms_list[0][i]
    sieve = [True] * (first + 1)
    result = -1
    for p in reversed_perms_list:
        if p[0] == 0 or p[order[-1]] % 2 == 0 or p[order[-1]] == 5:
            continue
        first = 0
        for i in order:
            first *= 10
            first += p[i]
        eratosthenes(sieve, first)
        if sieve[first] is True:
            result = first
            break
    print(result)
    # print(d, kinds_count, counter)
    return


if __name__ == "__main__":
    main()
