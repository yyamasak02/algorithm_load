x, y = map(int, input().split())

cal = []
 
for i in range(1, 7):
    for j in range(1, 7):
        a = i + j
        b = abs(i - j)
        cal.append((a, b))

pos = 0
for i in range(len(cal)):
    if cal[i][0] >= x or cal[i][1] >= y:
        pos += 1
print(pos / len(cal))
