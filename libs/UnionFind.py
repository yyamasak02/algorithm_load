class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.par: list[int] = [-1 for _ in range(n + 1)]
        self.siz: list[int] = [1 for _ in range(n + 1)]

    def root(self, n: int) -> int:
        while self.par[n] != -1:
            n = self.par[n]
        return n

    def unite(self, u: int, v: int) -> bool:
        u_root: int = self.root(u)
        v_root: int = self.root(v)
        if u_root == v_root:
            return True
        if self.siz[u_root] < self.siz[v_root]:
            u_root, v_root = v_root, u_root
        self.par[v_root] = u_root
        self.siz[u_root] += self.siz[v_root]
        return False

    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)

    @property
    def roots(self) -> list[int]:
        roots: list[int] = []
        for i in range(1, self.n + 1):
            if self.par[i] == -1:
                roots.append(i)
        return roots

    def size(self, v: int) -> int:
        return self.siz[self.root(v)]
