def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] -= 1
    visited = [False] * N
    result = [-1] * N
    for i in range(N):
        if visited[i] == True:
            continue
        tmp = i
        group = []
        while visited[tmp] != True:
            visited[tmp] = True
            group.append(tmp)
            tmp = A[tmp]
        if result[tmp] == -1:
            target = tmp + 1
        else:
            target = result[tmp]
        for c in group:
            result[c] = target
    print(*result)
    return


if __name__ == "__main__":
    main()
