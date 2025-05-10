n = int(input())
A = list(map(int, input().split()))
res = 0

col_list = [0 for i in range(n)]
for i in range(n):
    if i == 0:
        col_list[i] = A[i]
    else:
        col_list[i] = col_list[i-1] + A[i]

for i in range(n-1):
    moto = A[i]
    kaeru = col_list[n-1] - col_list[i]
    res += moto * kaeru
print(res) 
