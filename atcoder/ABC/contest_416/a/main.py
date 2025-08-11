# a = list(map(int, input().split()))
# b = int(input())
# c = input()
n, ll, r = map(int, input().split())
s = input()
for i in range(ll - 1, r):
    if s[i] != "o":
        print("No")
        exit()
print("Yes")
