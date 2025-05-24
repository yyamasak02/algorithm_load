def get_max_xor(fields, w, h):
    max_xor = 0
    current_xor = 0
    for i in range(h):
        for j in range(w):
            current_xor ^= fields[i][j]
    max_xor = max(max_xor, current_xor)
    
    for mask in range(1 << (h * w)):
        used = [[False for _ in range(w)] for _ in range(h)]
        valid = True
        domino_count = 0
        for i in range(h):
            for j in range(w):
                if not valid:
                    break
                pos = i * w + j
                if (mask >> pos) & 1:
                    if j + 1 < w and not used[i][j] and not used[i][j+1]:
                        used[i][j] = used[i][j+1] = True
                        domino_count += 1
                    elif i + 1 < h and not used[i][j] and not used[i+1][j]:
                        used[i][j] = used[i+1][j] = True
                        domino_count += 1
                    else:
                        valid = False
                        break
        if not valid:
            continue
        current_xor = 0
        for i in range(h):
            for j in range(w):
                if not used[i][j]:
                    current_xor ^= fields[i][j]
        max_xor = max(max_xor, current_xor)
    return max_xor

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            print(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    backtrack('', 0, 0)

if __name__ == "__main__":
    h, w = map(int, input().split())
    fields = []
    for _ in range(h):
        a = list(map(int, input().split()))
        fields.append(a)
    res = get_max_xor(fields, w, h)
    print(res)
    n = int(input())
    generate_parentheses(n)