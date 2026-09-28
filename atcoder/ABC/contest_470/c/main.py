def main():
    N, Q = map(int, input().split())
    added_indexes = set()
    values = [0] * (N + 1)
    ans = 0
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            ans ^= values[query[1]] ^ (values[query[1]] + 1)
            if values[query[1]] == 0:
                added_indexes.add(query[1])
            values[query[1]] += 1
        else:
            nxt = set()
            for index in added_indexes:
                ans ^= values[index] ^ (values[index] - 1)
                if values[index] != 1:
                    nxt.add(index)
                values[index] -= 1
            added_indexes = nxt
        print(ans)
    return


if __name__ == "__main__":
    main()
