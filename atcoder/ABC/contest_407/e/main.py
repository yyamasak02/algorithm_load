def generate_parentheses(n):
    result = []
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    backtrack('', 0, 0)
    return result

def solve(n, a, length, patterns):
    ans = sum(a[:n])
    for s in patterns:
        tmp = 0
        for index, c in enumerate(s):
            if c == "(":
                tmp += a[index]
        ans = max(ans, tmp)
    return ans

    return

if __name__ == "__main__":
    t: int = int(input())
    patterns_dict = {}
    for _ in range(t):
        n = int(input())
        if not n in patterns_dict:
            patterns_dict[n] = generate_parentheses(n)
        a = []
        for _ in range(2 * n):
            a.append(int(input()))
        length = 2 * n
        print(solve(n, a, length, patterns_dict[n]))
