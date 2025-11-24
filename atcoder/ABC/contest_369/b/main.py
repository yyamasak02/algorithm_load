def main():
    left_hand = None
    right_hand = None
    result = 0
    n = int(input())
    for _ in range(n):
        query = input().split()
        a = int(query[0])
        if query[1] == "L":
            if left_hand is None:
                left_hand = a
            result += abs(a - left_hand)
            left_hand = a
        else:
            if right_hand is None:
                right_hand = a
            result += abs(a - right_hand)
            right_hand = a
    print(result)
    return


if __name__ == "__main__":
    main()
