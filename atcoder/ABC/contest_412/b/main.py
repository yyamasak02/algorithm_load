s = input()
t = input()
len_s = len(s)
for i in range(1, len_s):
    ord_s = ord(s[i])
    if ord_s >= 65 and ord_s <= 90:
        if s[i-1] not in t:
            print("No")
            exit()
print("Yes")