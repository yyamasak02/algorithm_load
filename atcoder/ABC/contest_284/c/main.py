def mapping_node(node_dict, visited_flag, start):
	if visited_flag[start]:
		return
	visited_flag[start] = True
	if start not in node_dict:
		return
	for node in node_dict[start]:
		mapping_node(node_dict, visited_flag, node)

if __name__ == "__main__":
	n,m = map(int, input().split())
	node_dict: dict[int, set] = {}
	visited_flag = [False for _ in range(n+1)]
	for _ in range(m):
		u,v = map(int, input().split())
		if u not in node_dict:
			node_dict[u] = set()
		node_dict[u].add(v)
	ans: int = 0
	for i in range(n):
		if not visited_flag[i + 1]:
			ans += 1
			if i + 1 in node_dict:
				mapping_node(node_dict, visited_flag, i + 1)
	print(ans)
