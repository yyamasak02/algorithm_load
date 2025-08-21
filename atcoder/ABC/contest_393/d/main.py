n: int = int(input())
s: str = input()
one_count: int = s.count("1")
result: int = 0
tmp_one_count: int = 0
for i in range(n):
    if s[i] == "0":
        result += min(tmp_one_count, one_count - tmp_one_count)
    else:
        tmp_one_count += 1
print(result)
