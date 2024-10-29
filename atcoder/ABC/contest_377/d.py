# https://atcoder.jp/contests/abc377/tasks/abc377_d

N, M = map(int, input().split())
section = [0 for i in range(M+1)]
ans = 0
columtive = 0
start,end = -1, 0

def cal_avail(start, end):
    kosuu = end - start
    print(kosuu)
    return (kosuu * (kosuu * 1)) // 2

for _ in range(N):
    L,R = map(int, input().split())
    section[L] += 1
    section[R] -= 1

print(section)
for i in range(M):
    columtive += section[i+1]
    if columtive == 0 and start == -1:
        start = i
    elif columtive != 0:
        if start != -1:
            ans += cal_avail(start, i)
            start = -1

if columtive == -1:
    ans += cal_avail(start, M)
print(ans)
        