"""
方針としては、0と1のケースで小さい手数のほうを出力する
その際に、真ん中から左は左側で処理、右は右側で処理するのが効率的になるのでその前提で計算をする
"""


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().rstrip()
        if s[0] == "0":
            c0, c1, prev, si = 1, 0, "0", 0
        else:
            c0, c1, prev, si = 0, 1, "1", 0
        m0, m1 = 0, 0
        for i in range(1, n):
            if s[i] == "0":
                c0 += 1
            else:
                c1 += 1
            if prev != s[i]:
                if prev == "0":
                    m0 = max(m0, i - si)
                else:
                    m1 = max(m1, i - si)
                prev = s[i]
                si = i
        if prev == "0":
            m0 = max(m0, i - si + 1)
        else:
            m1 = max(m1, i - si + 1)
        zero = 2 * (c0 - m0) + c1
        one = 2 * (c1 - m1) + c0
        print(min(zero, one))
    return


if __name__ == "__main__":
    main()
