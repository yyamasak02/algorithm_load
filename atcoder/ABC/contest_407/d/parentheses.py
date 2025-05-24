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

if __name__ == "__main__":
    n = int(input())
    patterns = generate_parentheses(n)
    for pattern in patterns:
        print(pattern) 