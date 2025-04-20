q = int(input())
quene = []
for _ in range(q):
    s = input()
    if s.startswith('1'):
        quene.append(int(s[2::]))
    if s.startswith('2'):
        print(quene.pop(0))