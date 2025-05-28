
def solve(whites, w_count, blacks, b_count):
    columtive_blacks = [0]
    columtive_whites = [0]
    ans = 0
    for i in range(b_count):
        columtive_blacks.append(columtive_blacks[i] + blacks[i])
    for i in range(w_count):
        columtive_whites.append(max(columtive_whites[i], columtive_whites[i] + whites[i]))
    for i in range(b_count+1):
        tmp = i
        if i >= w_count:
            tmp = w_count
        ans = max(ans, columtive_blacks[i] + columtive_whites[tmp])
    return ans
if __name__ == "__main__":
    n,m = map(int, input().split())
    b = list(map(int, input().split()))
    w = list(map(int, input().split()))
    b.sort(reverse=True)
    w.sort(reverse=True)
    print(solve(w, m, b, n))
 
