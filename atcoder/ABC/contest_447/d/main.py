from bisect import bisect_left
from collections import deque


def main():
    S = input()
    a_list = []
    b_list = deque()
    c_list = []
    size_s = len(S)
    for i in range(size_s):
        if S[i] == "A":
            a_list.append(i)
        if S[i] == "B":
            b_list.append(i)
        if S[i] == "C":
            c_list.append(i)
    counter = 0
    size_c = len(c_list)
    start_a, start_c = 0, 0
    already = set()
    while b_list:
        index = b_list.popleft()
        # print("target b index: ", index)
        # print("target a_list: ", a_list)
        # print("target c_list: ", c_list)
        # print("----------------------------")
        # print(start_c)
        a_index, c_index = (
            bisect_left(a_list, index, start_a),
            bisect_left(c_list, index, start_c),
        )
        # print(c_index)
        print(a_index, c_index)
        if a_index != start_a and c_index != size_c and start_c <= size_c - 1:
            counter += 1
            start_a += 1
            if start_c == c_index:
                start_c += 1
            else:
                start_c = min(size_c - 1, c_index)
    print(counter)
    return


if __name__ == "__main__":
    main()
