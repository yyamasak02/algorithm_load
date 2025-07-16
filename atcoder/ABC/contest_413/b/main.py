n = int(input())
S = []
for _ in range(n):
    S.append(input())

s_set = set()
for i in range(n-1):
    for j in range(i+1, n):
        s_set.add(S[i]+S[j])
        s_set.add(S[j]+S[i])
# print(s_set)
print(len(s_set))