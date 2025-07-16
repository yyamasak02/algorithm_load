def base_to_n(num_10: int, n: int):
    str_n = ''
    while num_10:
        if num_10 % n>=10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return (int(str_n[::-1]), len(str_n))

def is_rolling(n_str: str, length: int) -> bool:
    return n_str == n_str[::-1]
def solve():
    a = int(input())
    n = int(input())
    n_len = len(str(n))
    ans = 0
    for num in range(1, min(10, n + 1)):
        if num > n:
            break
        base_n, base_len = base_to_n(num, a)
        if is_rolling(str(base_n), base_len) and is_rolling(str(num), len(str(num))):
            ans += num
    if n_len >= 3:
        for half_len in range(1, (n_len // 2) + 1):
            max_prefix = 10 ** half_len - 1
            min_prefix = 10 ** (half_len - 1)
            for prefix in range(min_prefix, max_prefix + 1):
                num = prefix * (10 ** half_len) + int(str(prefix)[::-1])
                if num <= n:            
                    base_n, base_len = base_to_n(num, a)
                    if is_rolling(str(base_n), base_len):
                        ans += num
                else:
                    break
                for center in range(10):
                    num = prefix * (10 ** (half_len + 1)) + center * (10 ** half_len) + int(str(prefix)[::-1])
                    if num > n:
                        break   
                    base_n, base_len = base_to_n(num, a)
                    if is_rolling(str(base_n), base_len):
                        ans += num
    return ans

if __name__ == "__main__":
    print(solve())
