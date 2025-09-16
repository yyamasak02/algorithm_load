from collections import deque


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


if __name__ == "__main__":
    n, m = map(int, input().split())
    uf: UnionFind = UnionFind(n)
    remain_cables: list[tuple] = []
    roots: list[int] = None
    query: tuple = None
    flg: bool = None
    d: dict = None
    index: int = 0
    tmp: int = 1

    for i in range(m):
        query = tuple(map(int, input().split()))
        flg = uf.unite(*query)
        if flg is True:
            remain_cables.append((*query, i + 1))
    d = {root: {"len": 0, "deque": deque()} for root in uf.roots}
    for query in remain_cables:
        root: int = uf.root(query[0])
        d[root]["deque"].append(query)
        d[root]["len"] += 1

    sorted_items: list[tuple] = sorted(
        d.items(), key=lambda x: x[1]["len"], reverse=True
    )
    required_count = len(sorted_items) - 1
    ans = {"len": required_count, "list": []}

    while required_count > 0:
        que: deque = sorted_items[index][1]["deque"]
        while required_count > 0 and que:
            query = que.popleft()
            ans["list"].append((query[2], query[0], sorted_items[tmp][0]))
            tmp += 1
            required_count -= 1
        index += 1
    print(ans["len"])
    for query in ans["list"]:
        print(*query)
