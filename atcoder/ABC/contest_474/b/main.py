def main():
    N = int(input())
    P = list(map(int, input().split()))
    is_invalid = False
    for i in range(N):
        number = i // 10
        if not (number * 10 + 1) <= P[i] <= ((number + 1) * 10):
            # print(i, P[i])
            is_invalid = True
            break
    if is_invalid is True:
        print("No")
    else:
        print("Yes")
    return


if __name__ == "__main__":
    main()
