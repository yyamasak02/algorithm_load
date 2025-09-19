q = "".join(input().split())
c = "12345"
for i in range(4):
    swap_s = q[0:i] + q[i + 1 : i + 2] + q[i : i + 1] + q[i + 2 : 5]
    if swap_s == c:
        print("Yes")
        break
else:
    print("No")
