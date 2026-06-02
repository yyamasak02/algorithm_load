def main():
    N, K = map(int, input().split())
    L = []
    a_list = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        L.append(tmp[0])
        a_list.append(tmp[1::])
    C = list(map(int, input().split()))
    index, counter = 0, 0
    while counter < K:
        Li = L[index]
        Ai = a_list[index]
        Ci = C[index]
        if (counter + Ci * Li) < K:
            counter += Ci * Li
            index += 1
            continue
        target_index = K - counter
        # print(Li, Ai, Ci)
        print(Ai[(target_index % Li) - 1])
        break
    return


if __name__ == "__main__":
    main()
