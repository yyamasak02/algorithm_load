n = int(input())
a = ['-' for _ in range(n)]
if n % 2 == 0:
	a[n//2 - 1] = '='
	a[n//2] = '='
else:
	a[n//2] = '='
print(''.join(a))