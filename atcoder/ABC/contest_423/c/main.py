n, r = map(int, input().split())
ll = list(map(int, input().split()))
top_left_open, top_right_open = None, None
for i in range(n):
    if ll[i] == 0:
        if i < r and top_left_open is None:
            top_left_open = i
        elif i >= r:
            top_right_open = i
left_close = sum(ll[top_left_open:r]) if top_left_open is not None else 0
left_open = (r - top_left_open) - left_close if top_left_open is not None else 0
right_close = sum(ll[r : top_right_open + 1]) if top_right_open is not None else 0
right_open = (top_right_open - r + 1) - right_close if top_right_open is not None else 0
ans = left_open + (left_close * 2) + right_open + (right_close * 2)
print(ans)
