import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s1 = s[0]
    sn = s[n-1]
    if sn <= 2 * s1:
        print(2)
    else:
        nokori = sorted(s[1:n-1])
        current_size = s1
        domino_count = 1
        while current_size * 2 < sn:
            target = 2 * current_size
            index = bisect.bisect_right(nokori, target)
            if index == 0:
                print(-1)
                break
            current_size = nokori[index - 1]
            domino_count += 1
            nokori.pop(index - 1)
        else:
            domino_count += 1
            print(domino_count)