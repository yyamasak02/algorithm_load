n, q = map(int, input().split())
s = [i for i in range(n)]
h = [1 for _ in range(n)]
ans = 0
for _ in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 2:
        print(ans)
    else:
        bird_index = query[1] - 1
        new_bird_pos = query[2] - 1
        old_bird_pos = s[bird_index]
        old_bird_pos_num = h[old_bird_pos]
        if old_bird_pos_num == 2:
            ans -= 1
        h[old_bird_pos] -= 1
        s[bird_index] = new_bird_pos
        h[new_bird_pos] += 1
        if h[new_bird_pos] == 2:
            ans += 1
