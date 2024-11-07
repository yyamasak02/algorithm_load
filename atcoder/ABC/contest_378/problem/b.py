# https://atcoder.jp/contests/abc378/tasks/abc378_b

N = int(input())
trash_list: list = [0]

for _ in range(N):
    node: dict = {"q": 0, "r": 0}
    q,r = map(int, input().split())
    node["q"] = q
    node["r"] = r
    trash_list.append(node)

Q = int(input())
for _ in range(Q):
	t,d = map(int, input().split())
	tq,tr = trash_list[t]["q"], trash_list[t]["r"]

	res1: int = (d // tq) * tq + tr
	res2: int = ((d // tq) + 1) * tq + tr
	if (res1 >= d):
		print(res1)
	else:
		print(res2)