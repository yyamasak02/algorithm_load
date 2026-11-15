def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        values = []
        for i in range(N - 1):
            x_i = X[i] if S[i] == "S" else 0
            x_i_1 = X[i + 1] if S[i + 1] == "R" else 0
            values.append(Y[i] - (x_i + x_i_1))
        odd_numbers = []
        odd_value = 0
        even_numbers = []
        even_value = 0
        for i in range(N - 1):
            if (i + 1) % 2 == 0 and values[i] > 0:
                even_value += values[i]
                even_numbers.append(i)
            if (i + 1) % 2 == 1 and values[i] > 0:
                odd_value += values[i]
                odd_numbers.append(i)
        print(X)
        print(Y)
        print(values)
        print("Even Number: ", even_numbers)
        print("Even Value: ", even_value)
        print("Odd Number: ", odd_numbers)
        print("Odd Value: ", odd_value)
        print("------------" * 2)
    return


if __name__ == "__main__":
    main()
