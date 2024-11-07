# https://atcoder.jp/contests/abc378/tasks/abc378_a

def getNum(d: dict, num: int):
	if (d[num] == 4):
		return 2
	elif (d[num] >= 2):
		return 1
	return 0

di: dict = {1:0, 2:0, 3:0, 4:0}
a,b,c,d = map(int, input().split())
ans: int = 0
nokori = 4

di[a] += 1
di[b] += 1
di[c] += 1
di[d] += 1
ans += getNum(di, 1)
ans += getNum(di, 2)
ans += getNum(di, 3)
ans += getNum(di, 4)
print(ans)


