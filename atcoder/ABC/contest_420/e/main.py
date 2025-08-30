class UnionFind:
    def __init__(self, n: int) -> None:
        self.par: list[int] = [-1 for i in range(n + 1)]
        self.siz: list[int] = [1 for i in range(n + 1)]
        self.blacks: list[int] = [0 for i in range(n + 1)]
        self.colors: list[bool] = [False for i in range(n + 1)]

    def root(self, n: int) -> int:
        while self.par[n] != -1:
            n = self.par[n]
        return n

    def unite(self, u: int, v: int) -> None:
        u_root: int = self.root(u)
        v_root: int = self.root(v)
        if u_root == v_root:
            return
        if u_root > v_root:
            self.par[v_root] = u_root
            self.siz[u_root] += self.siz[v_root]
            self.blacks[u_root] += self.blacks[v_root]
        else:
            self.par[u_root] = v_root
            self.siz[v_root] += self.siz[u_root]
            self.blacks[v_root] += self.blacks[u_root]

    def add(self, u: int) -> None:
        if self.colors[u] is True:
            val = -1
        else:
            val = 1
        self.colors[u] = not self.colors[u]
        self.blacks[self.root(u)] += val

    def has_black(self, u: int) -> bool:
        return self.blacks[self.root(u)] > 0


if __name__ == "__main__":
    n, q = map(int, input().split())
    uf: UnionFind = UnionFind(n)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            uf.unite(u=query[1], v=query[2])
        elif query[0] == 2:
            uf.add(u=query[1])
        else:
            print("Yes" if uf.has_black(u=query[1]) is True else "No")
