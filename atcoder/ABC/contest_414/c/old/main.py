def is_collect(s):
    return s == s[::-1]

def to_base_a(n, a):
    if n == 0:
        return "0"
    
    digits = []
    while n > 0:
        digits.append(str(n % a))
        n //= a
    
    return "".join(digits[::-1])

def generate(n):
    x = []
    
    for i in range(1, 10):
        if i <= n:
            x.append(i)
    length = 2
    while True:
        half_len = length // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len
        for i in range(start, end):
            prefix = str(i)
            if length % 2 == 0:
                palindrome = int(prefix + prefix[::-1])
            else:
                for center in range(10):
                    palindrome = int(prefix + str(center) + prefix[::-1])
                    if palindrome <= n:
                        x.append(palindrome)
                    else:
                        break
                continue
            if palindrome <= n:
                x.append(palindrome)
            else:
                break
        length += 1
        if 10 ** (length - 1) > n:
            break
    return x

if __name__ == "__main__":
    a = int(input())
    n = int(input())
    x = generate(n)
    ans = 0
    
    for p in x:
        base_a_str = to_base_a(p, a)
        if is_collect(base_a_str):
            ans += p
    
    print(ans)
