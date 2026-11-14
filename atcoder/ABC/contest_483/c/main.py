def main():
    N, M = map(int, input().split())
    votes = [tuple(map(int, input().split())) for _ in range(M)]
    second_votes = [{} for _ in range(N + 1)]
    normal = [0] * (N + 1)
    for vote in votes:
        normal[vote[0]] += 1
        if vote[1] not in second_votes[vote[0]]:
            second_votes[vote[0]][vote[1]] = 0
        second_votes[vote[0]][vote[1]] += 1
    tmp = sorted([(normal[i], i) for i in range(1, N + 1)], key=lambda x: (-x[0], x[1]))
    first, second = tmp[0][1], tmp[1][1]
    for i in range(1, N + 1):
        canditate_d = second_votes[i]
        target = first if first != i else second
        counter = (
            normal[target]
            if target not in canditate_d
            else normal[target] + canditate_d[target]
        )
        for key, additional in canditate_d.items():
            if counter < normal[key] + additional:
                target, counter = key, normal[key] + additional
            if counter == normal[key] + additional and key < target:
                target, counter = key, normal[key] + additional
        print(target)
    # print(normal, second_votes)
    return


if __name__ == "__main__":
    main()
