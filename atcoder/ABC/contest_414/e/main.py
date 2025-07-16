def solve():
    N = int(input())
    MOD = 998244353
    
    count = 0
    
    # 調和級数の性質を利用
    # b ≤ √N の場合: 直接計算
    # b > √N の場合: まとめて計算
    
    sqrt_n = int(N ** 0.5)
    
    # b ≤ √N の場合
    for b in range(1, sqrt_n + 1):
        q = N // b
        r = N % b
        total_a = (b - 1) * q + min(r, b - 1)
        count += total_a
        count %= MOD
    
    # b > √N の場合
    # 各qに対して、対応するbの範囲をまとめて計算
    for q in range(1, sqrt_n + 1):
        # q = N // b を満たすbの範囲: N // (q + 1) < b ≤ N // q
        min_b = N // (q + 1) + 1
        max_b = N // q
        
        # この範囲のbは全て同じqを持つ
        if min_b <= max_b:
            for b in range(max(min_b, sqrt_n + 1), max_b + 1):
                r = N % b
                total_a = (b - 1) * q + min(r, b - 1)
                count += total_a
                count %= MOD
    
    print(count)

if __name__ == "__main__":
    solve()
