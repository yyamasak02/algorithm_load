import sys
from bisect import bisect_right


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    bird_dic, counter = {}, 0
    birds = []
    for _ in range(N):
        a, d, b = map(int, input().split())
        if d == 1:
            if b not in bird_dic:
                bird_dic[b] = 0
            bird_dic[b] += 1
            if bird_dic[b] == 1:
                counter += 1
        else:
            if a not in bird_dic:
                bird_dic[a] = 0
            bird_dic[a] += 1
            if bird_dic[a] == 1:
                counter += 1
            birds.append((a, d, b))
    birds.sort(key=lambda x: x[1])
    prev = 0
    for i in range(M):
        end = bisect_right(birds, i + 1, key=lambda x: x[1])
        for j in range(prev, end):
            a, _, b = birds[j]
            bird_dic[a] -= 1
            if bird_dic[a] == 0:
                counter -= 1
            if b not in bird_dic:
                bird_dic[b] = 0
            bird_dic[b] += 1
            if bird_dic[b] == 1:
                counter += 1
            prev = end
        print(counter)
    return


if __name__ == "__main__":
    main()
