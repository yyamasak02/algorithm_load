def main():
    N, X = input().split()
    N = int(N)
    d = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    seats = [[] for _ in range(5)]
    for _ in range(N):
        S = input()
        for i in range(5):
            seats[i].append(S[i])
    result = "Yes" if "o" in seats[d[X]] else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
