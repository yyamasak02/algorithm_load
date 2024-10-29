N, M = map(int, input().split())
picker_set = set()

def add_if_true(a, b, N, picker_set):
    if a >= 1 and a <= N:
        if b >= 1 and b <= N:
            ans = str(a).zfill(10) + str(b).zfill(10)
            picker_set.add(ans)

for _ in range(M):
    a,b = map(int, input().split())
    add_if_true(a, b, N, picker_set)
    
    add_if_true(a+2, b+1, N, picker_set)
    add_if_true(a+2, b-1, N, picker_set)
    
    add_if_true(a+1, b+2, N, picker_set)
    add_if_true(a+1, b-2, N, picker_set)
    
    add_if_true(a-2, b+1, N, picker_set)
    add_if_true(a-2, b-1, N, picker_set)

    add_if_true(a-1, b-2, N, picker_set)
    add_if_true(a-1, b+2, N, picker_set)
print(N*N - len(picker_set))
