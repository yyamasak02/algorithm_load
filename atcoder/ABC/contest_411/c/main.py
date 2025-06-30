n,q = map(int, input().split())
a = list(map(int, input().split()))
ans = [False for _ in range(n)]
res = 0

if n == 1:
    for i in range(q):
        q1 = a[i] - 1
        ans[q1] = not ans[q1]
        print(1 if ans[q1] == True else 0)
else:
    for i in range(q):
        q1 = a[i] - 1
        ans[q1] = not ans[q1]
        if q1 == 0:
            if ans[q1] == True:
                if ans[q1+1] == False:
                    res += 1
            else:
                if ans[q1+1] == False:
                    res -= 1
        elif q1 == n-1:
            if ans[q1] == True:
                if ans[q1-1] == False:
                    res += 1
            else:
                if ans[q1-1] == False:
                    res -= 1
        else:
            if ans[q1] == True:
                if ans[q1-1] == False and ans[q1+1] == False:
                    res += 1
                elif ans[q1-1] == True and ans[q1+1] == True:
                    res -= 1
            else:
                if ans[q1-1] == True and ans[q1+1] == True:
                    res += 1
                elif ans[q1-1] == False and ans[q1+1] == False:
                    res -= 1
        print(res)



