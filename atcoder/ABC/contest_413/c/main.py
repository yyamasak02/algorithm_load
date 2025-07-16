from dataclasses import dataclass

@dataclass
class Pair:
    num: int
    count: int


q = int(input())
quene = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        x = query[2]
        quene.append(
            Pair(
                num=x,
                count=c
            )
        )
    else:
        k = query[1]
        start = 0
        ans = 0
        while k > 0:
            print("try")
            if quene[start].count > k:
                ans += quene[start].num * k
                quene[start].count -= k
                break
            else:
                nokori = quene.pop(0)
                ans += nokori.num * nokori.count
                k -= nokori.count
            start += 1
        print(ans)


