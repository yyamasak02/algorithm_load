N = int(input())
A = list(map(int, input().split()))
res = 0
for i in range(N-2):
    if A[i] == A[i+1] and A[i] == A[i+2]:
        print("Yes")
        exit(0)
print("No")