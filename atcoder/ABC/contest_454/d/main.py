def main():
    T = int(input())

    def delete_parentheses(S):
        tmp_list = S.split("xx")
        result_set = []
        chunks = len(tmp_list)
        prev_left, prev_right, prev_deletable = 0, 0, 0
        for i in range(chunks):
            s = tmp_list[i]
            size = len(s)
            left, right = 0, 0
            while left < size and s[size - left - 1] == "(":
                left += 1
            while right < size and s[right] == ")":
                right += 1
            deletable = min(prev_left, right)
            if i != 0:
                target_str = tmp_list[i - 1][
                    prev_deletable : len(tmp_list[i - 1]) - deletable
                ]
                result_set.append(f"{target_str}xx")
            prev_left, prev_right, prev_deletable = left, right, deletable
        target_str = tmp_list[-1][prev_deletable::]
        result_set.append(f"{target_str}")
        return "".join(result_set)

    for _ in range(T):
        A = delete_parentheses(input())
        B = delete_parentheses(input())
        if A == B:
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
