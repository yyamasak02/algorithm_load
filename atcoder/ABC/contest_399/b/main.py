from dataclasses import dataclass

@dataclass
class Param:
	index: int
	value: int
	rank: int

n = int(input())
p = list(map(int, input().split()))
params: list[Param] = []

for i in range(n):
	param = Param(i, p[i], 0)
	params.append(param)
params.sort(key=lambda x: x.value, reverse=True)

rank: int = 1
for i in range(n):
	if i > 0 and params[i].value != params[i - 1].value:
		rank = i + 1
	params[i].rank = rank
params.sort(key=lambda x: x.index)
for i in range(n):
	print(params[i].rank)