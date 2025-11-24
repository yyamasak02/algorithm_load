def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ll = [0]
    for c in a:
        ll.append((ll[-1] + c) % m)
    for c in a:
        ll.append((ll[-1] + c) % m)
    ll.pop(0)
    mod_list = [0] * m
    result = 0
    for i in range(n):
        mod_list[ll[i]] += 1
    print(ll)
    for i in range(n, 2 * n):
        mod_list[ll[i - n]] -= 1
        result += mod_list[ll[i]]
        mod_list[ll[i]] += 1
    print(result)
    return


if __name__ == "__main__":
    main()
