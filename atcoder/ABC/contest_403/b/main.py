t = input()
u = input()
u_len = len(u)
t_len = len(t)

def check(t: str, u: str) -> bool:
    for i in range(t_len):
        if (t[i] == u[0]) or (t[i] == "?"):
            for j in range(u_len):
                if i+j >= t_len:
                    break
                if not(t[i+j] == u[j] or t[i+j] == "?"):
                    break
            else:
                return True
    return False

if check(t, u):
    print("Yes")
else:
    print("No")
