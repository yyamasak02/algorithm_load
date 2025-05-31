if __name__ == "__main__":
    n: int = int(input())
    box: list[list[str]] = [["." for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = n - i - 1
        if i <= j and (i+1) % 2 == 1:
            sig = "#"
            for a in range(i, j+1):
                for b in range(i, j+1):
                    if (a == i) or (a == j) or (b == i) or (b == j):
                        box[a][b] = sig 
    for i in range(n):
        print("".join(box[i]))


