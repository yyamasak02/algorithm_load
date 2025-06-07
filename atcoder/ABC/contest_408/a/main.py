if __name__ == "__main__":
    n,s = map(int , input().split())
    t = list(map(int , input().split()))
    diff = []
    t.insert(0, 0)
    for i in range(n):
        diff.append(t[i+1] - t[i])
    diff.sort(reverse=True)
    if len(diff) == 0:
        print("Yes")
    else:
        for i in range(len(diff)):
            if diff[i] > s:
                print("No")
                break
        else:
            print("Yes")

