def main():
    n, q = map(int, input().split())
    s = list(input())
    ans = 0
    for i in range(n - 2):
        if "".join(s[i : i + 3]) == "ABC":
            ans += 1
    for _ in range(q):
        query = input().split()
        index = int(query[0]) - 1
        if s[index] == "A":
            if index + 2 < n and "".join(s[index : index + 3]) == "ABC":
                ans -= 1
        elif s[index] == "B":
            if (
                index + 1 < n
                and index - 1 >= 0
                and "".join(s[index - 1 : index + 2]) == "ABC"
            ):
                ans -= 1
        elif s[index] == "C":
            if index - 2 >= 0 and "".join(s[index - 2 : index + 1]) == "ABC":
                ans -= 1

        s[index] = query[1]
        if s[index] == "A":
            if index + 2 < n and "".join(s[index : index + 3]) == "ABC":
                ans += 1
        elif s[index] == "B":
            if (
                index + 1 < n
                and index - 1 >= 0
                and "".join(s[index - 1 : index + 2]) == "ABC"
            ):
                ans += 1
        elif s[index] == "C":
            if index - 2 >= 0 and "".join(s[index - 2 : index + 1]) == "ABC":
                ans += 1
        print(ans)
    return


if __name__ == "__main__":
    main()
