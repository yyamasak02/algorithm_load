n, m = map(int, input().split())
scores = [[False] * n for i in range(m)]
answers = [0 for i in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == "1":
            scores[j][i] = True

# print(scores)
max_score = 0
for i in range(m):
    gokei = sum(scores[i])
    if gokei < n - gokei or gokei == n:
        winner = True
    else:
        winner = False
    for j in range(n):
        if scores[i][j] == winner:
            answers[j] += 1
            max_score = max(answers[j], max_score)

print(*[i + 1 for i in range(n) if answers[i] == max_score])
