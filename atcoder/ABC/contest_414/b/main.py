n = int(input())
s = ""
s_len = 0
for i in range(n):
    c,l = input().split()
    l = int(l)
    s_len += l
    if s_len > 100:
        break
    s = s + c*l

if s_len > 100:
    print("Too Long")
else:
    print(s)
