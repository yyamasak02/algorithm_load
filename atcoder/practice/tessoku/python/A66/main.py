class UnionFind:
    def __init__(self, n: int) -> None:
        self.par: list[int] = [-1 for i in range(n + 1)]
        self.siz: list[int] = [1 for i in range(n + 1)]

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
        else:
            self.par[u_root] = v_root
            self.siz[v_root] += self.siz[u_root]

    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)


if __name__ == "__main__":
    n, q = map(int, input().split())
    uf: UnionFind = UnionFind(n)
    for _ in range(q):
        query, u, v = map(int, input().split())
        if query == 1:
            uf.unite(u=u, v=v)
        else:
            print("Yes" if uf.same(u=u, v=v) is True else "No")
