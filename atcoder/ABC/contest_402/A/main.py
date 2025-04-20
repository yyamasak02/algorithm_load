a_ascii = ord('A')
z_ascii = ord('Z')

s = input()
ans = []
for s_char in s:
    if ord(s_char) >= a_ascii and ord(s_char) <= z_ascii:
        ans.append(s_char)
print("".join(ans))