def main():
    N, S, L = map(int, input().split())
    A = list(map(int, input().split()))
    round_trip_costs = [0] * (N - 1)
    _ = 0
    for i in range(S - 2, -1, -1):
        if i in [N - 1, S - 2]:
            round_trip_costs[i] = A[i] * 2
            continue
        round_trip_costs[i] = A[i] * 2 + round_trip_costs[i + 1]
    for i in range(S - 1, N - 1):
        if i in [0, S - 1]:
            round_trip_costs[i] = A[i] * 2
            continue
        print(i)
        round_trip_costs[i] = A[i] * 2 + round_trip_costs[i - 1]
    print(round_trip_costs)
    return


if __name__ == "__main__":
    main()
