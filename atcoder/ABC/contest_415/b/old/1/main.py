s = input()
len_s = len(s)
num = 0
prev = 0
for i in range(len_s):
    if s[i] == "#":
        num += 1
        flag = True
    else:
        flag = False
    if num % 2 == 1 and flag is True:
        prev = i + 1
    if num % 2 == 0 and flag is True:
        print(f"{prev},{i+1}")
