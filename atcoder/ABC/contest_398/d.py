n,r,c = map(int, input().split())
s = input()
field = [[0 for _ in range(n * 2 + 1)] for _ in range(n * 2 + 1)]
smocks = set()
ans = [0 for _ in range(n)]
center_index = (n, n)
route_index = (n, n)
smocks.add(route_index)
field[route_index[0]][route_index[1]] = 1
for index, sig in enumerate(s):
	if sig == 'N':
		r -= 1
		route_index = (route_index[0] - 1, route_index[1])
		smocks.add(route_index)
	elif sig == 'S':
		r += 1
		route_index = (route_index[0] + 1, route_index[1])
		smocks.add(route_index)
	elif sig == 'E':
		c += 1
		route_index = (route_index[0], route_index[1] + 1)
		smocks.add(route_index)
	elif sig == 'W':
		c -= 1
		route_index = (route_index[0], route_index[1] - 1)
		smocks.add(route_index)
	field[route_index[0]][route_index[1]] = 1
	if field[center_index[0] + r][center_index[1] + c] == 1:
		ans[index] = 1
for f in field:
	print(f)
print(''.join(map(str, ans)))