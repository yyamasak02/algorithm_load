def solve(h, w, fields):
    # 初期状態（ドミノなし）
    possible_domino = [0]
    
    # 縦横のドミノのパターン
    domino_vertical = (1 << w) + 1
    print(bin(domino_vertical))
    domino_horizontal = 3
    
    # 各マスについてドミノの配置を試す
    for i in range(h):
        for j in range(w):
            bit = i * w + j
            tmp = []
            for b in possible_domino:
                print(bin(b))
                # 横方向のドミノ
                if j + 1 < w and not (b & (domino_horizontal << bit)):
                    tmp.append(b | (domino_horizontal << bit))
                # 縦方向のドミノ
                if i + 1 < h and not (b & (domino_vertical << bit)):
                    tmp.append(b | (domino_vertical << bit))
            print(tmp)
            possible_domino.extend(tmp)
    
    # 各配置パターンに対してXORを計算
    ans = 0
    print(possible_domino)
    for b in possible_domino:
        now = 0
        for i in range(h):
            for j in range(w):
                bit = i * w + j
                if not (b & (1 << bit)):  # ドミノが置かれていないマス
                    now ^= fields[i][j]
        ans = max(ans, now)
    
    return ans

if __name__ == "__main__":
    h, w = map(int, input().split())
    fields = []
    for _ in range(h):
        a = list(map(int, input().split()))
        fields.append(a)
    print(solve(h, w, fields))