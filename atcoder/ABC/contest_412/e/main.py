def solve():
    L, R = map(int, input().split())
    
    # エラトステネスの篩で素数テーブルを作成
    max_n = R
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    # 素因数分解（素数テーブル利用）
    def factorize(n):
        factors = {}
        if n == 1:
            return factors
        
        for i in range(2, int(n**0.5) + 1):
            if not is_prime[i]:
                continue
            while n % i == 0:
                factors[i] = factors.get(i, 0) + 1
                n //= i
            if n == 1:
                break
        
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        
        return factors
    
    # LCM(1,2,...,L-1)の素因数を計算
    current_lcm_factors = {}
    for i in range(1, L):
        factors = factorize(i)
        for prime, power in factors.items():
            current_lcm_factors[prime] = max(current_lcm_factors.get(prime, 0), power)
    
    # 素因数の組み合わせを文字列として保存
    lcm_signatures = set()
    
    # LからRまで順次計算
    for n in range(L, R + 1):
        factors = factorize(n)
        
        # 新しい素因数があるかチェック
        for prime, power in factors.items():
            if current_lcm_factors.get(prime, 0) < power:
                current_lcm_factors[prime] = power
        
        # 素因数の組み合わせを文字列として保存
        signature = []
        for prime in sorted(current_lcm_factors.keys()):
            signature.append(f"{prime}^{current_lcm_factors[prime]}")
        lcm_signatures.add(" ".join(signature))
    
    print(len(lcm_signatures))

solve()
