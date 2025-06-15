import heapq
from collections import defaultdict

def main():
    # 入力
    N, M = map(int, input().split())
    
    # グラフの構築
    G = defaultdict(list)
    for _ in range(M):
        a, b, w = map(int, input().split())
        G[a].append((b, w))
    
    # 各頂点に対して、到達可能なXOR値の集合を管理
    xor_values = [set() for _ in range(N + 1)]
    xor_values[1].add(0)  # 始点のXOR値は0
    
    # 優先度付きキューでXOR値が小さい順に探索
    pq = [(0, 1)]  # (XOR値, 頂点)の形式
    
    while pq:
        current_xor, v = heapq.heappop(pq)
        
        # 現在の頂点から到達可能な頂点を探索
        for next_v, weight in G[v]:
            new_xor = current_xor ^ weight
            
            # 新しいXOR値が既に記録されている場合はスキップ
            if new_xor in xor_values[next_v]:
                continue
            
            # 新しいXOR値を記録
            xor_values[next_v].add(new_xor)
            heapq.heappush(pq, (new_xor, next_v))
    
    # 頂点Nに到達可能なXOR値の最小値を出力
    if not xor_values[N]:
        print(-1)
    else:
        print(min(xor_values[N]))

if __name__ == "__main__":
    main() 