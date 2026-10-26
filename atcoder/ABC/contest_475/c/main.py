def main():
    N, S, L = map(int, input().split())
    A = list(map(int, input().split()))
    round_trip_costs = [0] * (N - 1)
    for i in range(S - 2, -1, -1):
        if i in [N - 1, S - 2]:
            round_trip_costs[i] = A[i] * 2
            continue
        round_trip_costs[i] = A[i] * 2 + round_trip_costs[i + 1]
    for i in range(S - 1, N - 1):
        if i in [0, S - 1]:
            round_trip_costs[i] = A[i] * 2
            continue
        # print(i)
        round_trip_costs[i] = A[i] * 2 + round_trip_costs[i - 1]
    max_count = 0
    for i in range(S - 1, -1, -1):
        if i != S - 1 and round_trip_costs[i] > L:
            continue
        tmp_cost = round_trip_costs[i] if i != S - 1 else 0
        counter = S - i
        # print("tmp_cost, counter", tmp_cost, counter)
        for j in range(S - 1, N - 1):
            if tmp_cost + A[j] > L:
                break
            tmp_cost += A[j]
            counter += 1
            # print(A[j])
        # print("-------tmp_cost, counter", tmp_cost, counter)
        max_count = max(max_count, counter)
    for i in range(S - 2, N - 1):
        if i != S - 2 and round_trip_costs[i] > L:
            continue
        tmp_cost = round_trip_costs[i] if i != S - 2 else 0
        counter = i + 3 - S
        # print("tmp_cost, counter", tmp_cost, counter)
        for j in range(S - 2, -1, -1):
            if tmp_cost + A[j] > L:
                break
            tmp_cost += A[j]
            counter += 1
            # print(A[j])
        # print("-------tmp_cost, counter", tmp_cost, counter)
        max_count = max(max_count, counter)
    # print(round_trip_costs)
    print(max_count)
    return


if __name__ == "__main__":
    main()
