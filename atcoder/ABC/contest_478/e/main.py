import sys


class SCC:
    """Kosaraju法による強連結成分分解（頂点番号は0-indexed）。"""

    def __init__(self, n: int, edges: tuple[int, int] = ()) -> None:
        self.n = n
        self.adj: list[list[int]] = [[] for _ in range(n)]
        self.rev_adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        # 元の辺 u → v に対して、逆グラフには v → u を追加する。
        self.rev_adj[v].append(u)

    def _dfs_finish_order(
        self,
        u: int,
        graph: list[list[int]],
        visited: list[bool],
    ) -> list[int]:
        """渡されたグラフをDFSし、探索が終了した順に頂点を返す。

        グラフや訪問済み情報は変更しない。辺の反転もここでは行わない。
        """
        if visited[u]:
            return []
        discovered = {u}
        result = []

        # (頂点, 次に調べる隣接頂点の位置) を保持する。
        stack = [(u, 0)]
        while stack:
            u, index = stack[-1]
            if index == len(graph[u]):
                stack.pop()
                # 隣接頂点の探索がすべて終了したので記録する（帰りがけ順）。
                result.append(u)
                continue

            v = graph[u][index]
            stack[-1] = (u, index + 1)
            if visited[v] or v in discovered:
                continue
            discovered.add(v)
            stack.append((v, 0))

        return result

    def scc(self) -> list[list[int]]:
        """強連結成分のリストをトポロジカル順に返す。"""
        visited = [False] * self.n
        finish_order = []

        # 1. 元のグラフで、探索が終了した順序を求める。
        for i in range(self.n):
            if not visited[i]:
                reached = self._dfs_finish_order(i, self.adj, visited)
                finish_order.extend(reached)
                for v in reached:
                    visited[v] = True

        # 2. 辺を反転した逆グラフを使い、終了順の逆から探索を開始する。
        visited = [False] * self.n
        scc_list = []

        for u in reversed(finish_order):
            if not visited[u]:
                # 新たに到達した頂点が1つのSCC。成分内の頂点の順序は問わない。
                component = self._dfs_finish_order(u, self.rev_adj, visited)
                scc_list.append(component)
                for v in component:
                    visited[v] = True

        return scc_list


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    graph = SCC(N)
    lt: list[tuple[int, int]] = []
    for _ in range(Q):
        t, u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph.add_edge(u, v)
        if t:
            lt.append((u, v))

    # 強連結成分のトポロジカル順序に従って番号を付ける。
    ans = [0] * N
    for i, component in enumerate(graph.scc(), start=1):
        for x in component:
            ans[x] = i

    # t = 1 の辺の両端が同じ成分なら、厳密な大小関係を満たせない。
    for u, v in lt:
        if ans[u] == ans[v]:
            print("No")
            return

    print("Yes")
    print(*ans)


if __name__ == "__main__":
    main()
