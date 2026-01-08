n = int(input())
s = input()

ans = float("inf")
finish_index_odd = 0
finish_index_even = 1
odd_ans = 0
even_ans = 0
for i in range(2 * n):
    if s[i] == "A":
        # 偶数配列にAを置く
        odd_ans += abs(i - finish_index_odd)
        finish_index_odd += 2
        # 奇数配列にAを置く
        even_ans += abs(i - finish_index_even)
        finish_index_even += 2
print(min(even_ans, odd_ans))
