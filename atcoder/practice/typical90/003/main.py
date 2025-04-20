# n = int(input())
# begin = 0
# first_to = 0
# connect_list_passed: list[int] = [-1 for i in range(n+1)]
# connect_dict: dict[int, set] = {}
# connect_passed_dict: dict[int, set] = {i:[False for j in range(n+1)] for i in range(1, n+1)}

# def dfs(from_num, to_num, current_num):
#     if connect_passed_dict[from_num][to_num] == True:
#         return
#     if (current_num <= connect_list_passed[to_num]) or connect_list_passed[to_num] == -1:
#         connect_list_passed[to_num] = current_num
#     current_num = connect_list_passed[to_num]
#     connect_passed_dict[from_num][to_num] = True
#     connect_passed_dict[to_num][from_num] = True
#     for next_to_num in connect_dict[to_num]:
#         if connect_passed_dict[to_num][next_to_num] != True:
#         	dfs(to_num, next_to_num, current_num + 1)


# for _ in range(n-1):
#     a,b = map(int, input().split())
#     if not connect_dict.get(a):
#         connect_dict[a] = set()
#     if not connect_dict.get(b):
#         connect_dict[b] = set()
#     connect_dict[a].add(b)
#     connect_dict[b].add(a)

# for key, value in connect_dict.items():
#     if len(value) == 1:
#         begin = key
#         first_to = value.pop()
#         break
# dfs(begin, first_to, 1)
# print(max(connect_list_passed) + 1)

from collections import defaultdict, deque

def find_farthest(start, connect_dict):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])
    farthest_node = start

    while queue:
        current = queue.popleft()
        for neighbor in connect_dict[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
                if visited[neighbor] > visited[farthest_node]:
                    farthest_node = neighbor
    return farthest_node, visited[farthest_node]

n = int(input())
connect_dict = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    connect_dict[a].append(b)
    connect_dict[b].append(a)

# 1回目：適当なノード(1)から最も遠いノードを探す
node_a, _ = find_farthest(1, connect_dict)

# 2回目：そのノードから最大距離を調べる → 直径
_, diameter = find_farthest(node_a, connect_dict)

# 出力（距離 + 1）
print(diameter + 1)
