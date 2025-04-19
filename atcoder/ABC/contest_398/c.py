n = int(input())
a = list(map(int, input().split()))
max_value = -1
max_index = -2
ans = {}
for index, num in enumerate(a):
	if num in ans:
		ans[num].append(index)
	else:
		ans[num] = [index]
for key, value in ans.items():
	if len(value) == 1:
		if key > max_value:
			max_value = key
			max_index = value[0]
print(max_index + 1)