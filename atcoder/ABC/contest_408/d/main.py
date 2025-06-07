def solve(n, s):
    l = []
    diff = []
    start = -1
    end = -1
    for i in range(n):
        if s[i] == "1":
            if start == -1:
                start = i
                if end != -1:
                    diff.append(i - end)
        else:
            if start != -1:
                end = i
                l.append(end-start)
                start = -1
    if start != -1:
        l.append((n-start))
    print(l)
    print(diff)
    return None

if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n = int(input())
        s = input()
        print(solve(n, s))