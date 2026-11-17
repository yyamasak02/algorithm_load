from collections import deque


def main():
    def runLengthEncoding(string: str):
        result = []
        for char in string:
            if result and result[-1][0] == char:
                result[-1][1] += 1
            else:
                result.append([char, 1])
        return result

    S = input()
    run_length_result = runLengthEncoding(S)

    c_queue = deque()
    c_count = 0

    for i, (char, count) in enumerate(run_length_result):
        if char == "C":
            c_queue.append([i, count])
            c_count += count

    ans, a_count = 0, 0

    for i, (char, count) in enumerate(run_length_result):
        if char == "A":
            a_count += count

        elif char == "C":
            if c_queue and c_queue[0][0] == i:
                c_count -= c_queue.popleft()[1]

        elif char == "B":
            take = min(a_count, count, c_count)

            ans += take
            a_count -= take
            c_count -= take

            while take > 0:
                used = min(take, c_queue[0][1])
                c_queue[0][1] -= used
                take -= used

                if c_queue[0][1] == 0:
                    c_queue.popleft()

    print(ans)


if __name__ == "__main__":
    main()
