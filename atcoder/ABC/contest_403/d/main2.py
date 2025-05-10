n,d = map(int, input().split())
a = list(map(int, input().split()))
 
numbers = {}
for i in range(n):
    if a[i] not in numbers:
        numbers[a[i]] = 0
    numbers[a[i]] += 1

a = set(a)
a = list(a)
a.sort()
n = len(a)

# check (Ai - Aj) != d

import bisect
from dataclasses import dataclass

@dataclass
class Deleted:
    delete_nod: set
    delete_num: int
    same: int

def get_delete_dict(n, d, a) -> dict[int, Deleted]:
    deleted_dict= {}
    ans = 0
    for i in range(n):
        j = bisect.bisect_left(a, a[i] + d)
        if j < n and a[j] == a[i] + d:
            if a[i] not in deleted_dict:
                deleted_dict[a[i]] = Deleted(set(), 0, numbers[a[i]])
            deleted_dict[a[i]].delete_nod.add(a[j])
            deleted_dict[a[i]].delete_num += numbers[a[j]]
            if a[j] not in deleted_dict:
                deleted_dict[a[j]] = Deleted(set(), 0, numbers[a[j]])
            deleted_dict[a[j]].delete_nod.add(a[i])
            deleted_dict[a[j]].delete_num += numbers[a[i]]
    return deleted_dict

if __name__ == "__main__":
    ans: int = 0
    result = dict(sorted(get_delete_dict(n, d, a).items(), key=lambda x: (x[1].delete_num, -x[1].same), reverse=False))
    while len(result) > 0:
        key, value = result.popitem()
        ans += 1
        for i in value.delete_nod:
            if i in result:
                result[i].delete_nod.remove(key)
                result[i].delete_num -= numbers[key]
                if result[i].delete_num == 0:
                    result.pop(i)
    print(ans)
