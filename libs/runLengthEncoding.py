def runLengthEncoding(string: str) -> list[str, int]:
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


def runLengthDecoding(target: list[str, int]) -> str:
    return "".join(t[0] * t[1] for t in target)
