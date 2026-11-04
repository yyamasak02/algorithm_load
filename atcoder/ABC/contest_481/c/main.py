def main():
    Q = int(input())
    d = {}
    min_unassign_id = 1
    for _ in range(Q):
        query = input()
        if query not in d:
            d[query] = min_unassign_id
            min_unassign_id += 1
        print(d[query])

    return


if __name__ == "__main__":
    main()
