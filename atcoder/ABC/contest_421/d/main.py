from collections import deque


def main():
    rt, ct, ra, ca = map(int, input().split())
    # tkh_zone = (rt, ct)
    # aok_zone = (ra, ca)
    n, m, ll = map(int, input().split())
    converter = lambda x: (x[0], int(x[1]))
    tkh = deque(converter(tuple(map(str, input().split()))) for _ in range(m))
    aok = deque(converter(tuple(map(str, input().split()))) for _ in range(ll))
    print(tkh, aok)
    current = 0
    # TODO 実装
    # 先頭から取得し、横または縦が一致していて進む方向が逆の場合は、カウントできる
    # 完全一致から同じ方向の場合はその分加算できる
    # ステップの更新は、次の進行方向ステップ数のうち最小残進行量の方分進めれば
    # 効率的に進められる。
    while current < n:
        break
    return


if __name__ == "__main__":
    main()
