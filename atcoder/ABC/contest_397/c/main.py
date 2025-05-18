n = int(input())
A = list(map(int, input().split()))
migi = {}
hidari = {}
for a in A:
    if a not in migi:
        migi[a] = 0
    migi[a] += 1

migi_len = len(migi.keys())
hidari_len = len(hidari.keys())
ans = migi_len
for i in range(n):
    migi[A[i]] -= 1
    if migi[A[i]] == 0:
        migi_len -= 1
    if A[i] not in hidari:
        hidari[A[i]] = 0
    hidari[A[i]] += 1
    if hidari[A[i]] == 1:
        hidari_len += 1
    ans = max(ans, migi_len + hidari_len)
print(ans)