# a = list(map(int, input().split()))
# a = int(input())

a, b = map(int, input().split())
print(12 if (a + b) % 12 == 0 else (a + b) % 12)
