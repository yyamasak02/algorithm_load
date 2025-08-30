class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.black_count = [0] * n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self.parent[ra] > self.parent[rb]:
            ra, rb = rb, ra
        self.parent[ra] += self.parent[rb]
        self.parent[rb] = ra
        self.black_count[ra] += self.black_count[rb]

    def add(self, x, val):
        r = self.root(x)
        self.black_count[r] += val

    def has_black(self, x):
        r = self.root(x)
        return self.black_count[r] > 0


if __name__ == "__main__":
    n, q = map(int, input().split())
    uf = UnionFind(n)
    color = [0] * n

    ans = []
    for _ in range(q):
        s = input().split()
        t = int(s[0])
        if t == 1:
            u = int(s[1]) - 1
            v = int(s[2]) - 1
            uf.unite(u, v)
        elif t == 2:
            v = int(s[1]) - 1
            if color[v] == 0:
                color[v] = 1
                uf.add(v, 1)
            else:
                color[v] = 0
                uf.add(v, -1)
        else:
            v = int(s[1]) - 1
            if uf.has_black(v):
                ans.append("Yes")
            else:
                ans.append("No")

    for a in ans:
        print(a)
