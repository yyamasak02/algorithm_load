a = list(map(int, input().split()))
ans = {}
for i in a:
	if i in ans:
		ans[i] += 1
	else:
		ans[i] = 1
two = False
three = False
for key, value in ans.items():
	if value >= 3 and not three:
		three = True
	elif value >= 2 and not two:
		two = True
if two and three:
	print('Yes')
else:
	print('No')
