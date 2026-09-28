def main():
    N, M = map(int, input().split())
    d: dict[int, set] = {}
    requests = []
    counter = 0
    for i in range(M):
        a, b = map(int, input().split())
        requests.append((a, b))
        if a not in d:
            d[a] = set()
        if b not in d:
            d[b] = set()
        d[a].add(i)
        d[b].add(i)
    first = requests[0]
    pa, pb = set(), set()
    for i in range(1, M):
        if requests[i][0] != first[0] and requests[i][1] != first[0]:
            pa.add(requests[i][0])
            pa.add(requests[i][1])
        if requests[i][0] != first[1] and requests[i][1] != first[1]:
            if requests[i][0] != first[0]:
                pb.add(requests[i][0])
            if requests[i][1] != first[0]:
                pb.add(requests[i][1])
    pa = list(pa)
    pb = list(pb)
    # print(pa, pb)
    if not pa and not pb:
        counter += 2 * N - 3
    elif not pa:
        counter += N - 1
        for p in pb:
            if p == first[0]:
                continue
            if len(d[first[1]]) + len(d[p]) < M:
                continue
            if len(d[first[1]] | d[p]) == M:
                counter += 1
    elif not pb:
        for p in pa:
            if len(d[first[0]]) + len(d[p]) < M:
                continue
            if len(d[first[0]] | d[p]) == M:
                counter += 1
        counter += N - 2
    else:
        for p in pa:
            if len(d[first[0]]) + len(d[p]) < M:
                continue
            if len(d[first[0]] | d[p]) == M:
                counter += 1
        for p in pb:
            if p == first[0]:
                continue
            if len(d[first[1]]) + len(d[p]) < M:
                continue
            if len(d[first[1]] | d[p]) == M:
                counter += 1
    print(counter)
    return


if __name__ == "__main__":
    main()
