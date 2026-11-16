from collections import deque


def main():
    def runLengthEncoding(string: str):
        size = len(string)
        result = []
        target_char, pre_index = None, None
        for i in range(size):
            if target_char != string[i]:
                if pre_index is not None:
                    result.append((target_char, i - pre_index))
                target_char, pre_index = string[i], i
        result.append((target_char, size - pre_index))
        return result

    S = input()
    T = input()
    target_s = deque(runLengthEncoding(S))
    target_t = deque(runLengthEncoding(T))
    ans = 0
    is_error = False
    # print(target_s, target_t)
    while target_s or target_t:
        if not target_s:
            if target_t[0][0] == "A":
                ans += target_t[0][1]
                target_t.popleft()
            else:
                is_error = True
                break
        elif not target_t:
            if target_s[0][0] == "A":
                ans += target_s[0][1]
                target_s.popleft()
            else:
                is_error = True
                break
        else:
            if target_s[0][0] != "A" and target_t[0][0] != "A":
                if target_s[0][0] == target_t[0][0]:
                    c = target_s[0][0]
                    m = min(target_s[0][1], target_t[0][1])
                    rest_s = target_s[0][1] - m
                    rest_t = target_t[0][1] - m
                    target_s.popleft()
                    target_t.popleft()
                    if rest_s:
                        target_s.appendleft((c, rest_s))
                    if rest_t:
                        target_t.appendleft((c, rest_t))
                else:
                    is_error = True
                    break
            elif target_s[0][0] == "A" and target_t[0][0] != "A":
                ans += target_s[0][1]
                target_s.popleft()
            elif target_s[0][0] != "A" and target_t[0][0] == "A":
                ans += target_t[0][1]
                target_t.popleft()
            else:
                ans += abs(target_t[0][1] - target_s[0][1])
                target_t.popleft()
                target_s.popleft()
    if is_error is True:
        print(-1)
    else:
        print(ans)
    return


if __name__ == "__main__":
    main()
