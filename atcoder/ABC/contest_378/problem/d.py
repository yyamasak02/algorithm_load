# https://atcoder.jp/contests/abc378/tasks/abc378_d

'''
問題文：
	K回動ける通りは何通りあるか計算する。
	条件は以下
	①：同じ道を通らない
	②：障害物を通らない
	③：枠の範囲内を通る	
	④：出発地は、空いているところのどこか
所感：

回答：

'''

# TODO 続きやる

'''
	prev: 一個前の操作
	0: 上
	1: 下
	2: 左
	3: 右
'''
answer: int = 0
def movement(x: int, y: int, h: int, w: int, courses: list, k: int, prev: int, visited: list) -> int:
    global answer
    if k == 0:
        answer += 1
        return
    visited[y][x] = True
    if y - 1 >= 0 and courses[y - 1][x] == "." and not visited[y-1][x]:
        movement(x, y - 1, h, w, courses, k - 1, 0, visited)
    if y + 1 < h and courses[y + 1][x] == "." and not visited[y+1][x]:
        movement(x, y + 1, h, w, courses, k - 1, 1, visited)
    if x - 1 >= 0 and courses[y][x - 1] == "." and not visited[y][x-1]:
        movement(x - 1, y, h, w, courses, k - 1, 2, visited)
    if x + 1 < w and courses[y][x + 1] == "." and not visited[y][x+1]:
        movement(x + 1, y, h, w, courses, k - 1, 3, visited)
    visited[y][x] = False
    return

def solve(h: int, w: int, courses: list, k: int):
	starts: list = []
	ans: int = 0
	global answer

	for i in range(h):
		for j in range(w):
			if courses[i][j] == ".":
				starts.append((j, i))
	for x, y in starts:
		visited = [[False] * w for _ in range(h)]
		movement(x, y, h, w, courses, k, -1, visited)
		ans += answer
		answer = 0
	return ans

if __name__ == "__main__":
	H,W,K = map(int, input().split())
	courses = []
	for _ in range(H):
		courses.append(input())
	ans = solve(H,W,courses,K)
	print(ans)