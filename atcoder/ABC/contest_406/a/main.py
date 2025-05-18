A,B,C,D = map(int,input().split())

if (A > C):
    print("Yes")
elif (A == C):
    if (B > D):
        print("Yes")
    else:
        print("No")
else:
    print("No")