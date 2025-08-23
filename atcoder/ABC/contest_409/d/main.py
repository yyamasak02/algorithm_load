t: int = int(input())
for _ in range(t):
    n: int = int(input())
    s: str = input()
    swap_index: int = None
    insert_index: int = n - 1
    tmp = ["" for i in range(n)]
    for i in range(n - 1):
        if swap_index is None and s[i] > s[i + 1]:
            swap_index = i
        if swap_index is not None and s[swap_index] < s[i + 1]:
            insert_index = i
            break
    if swap_index is None:
        print(s)
        continue
    # print(swap_index, insert_index)
    for i in range(n):
        if i < swap_index:
            tmp[i] = s[i]
        elif i >= swap_index and i < insert_index:
            tmp[i] = s[i + 1]
        elif i == insert_index:
            tmp[i] = s[swap_index]
        else:
            tmp[i] = s[i]
    print("".join(tmp))
