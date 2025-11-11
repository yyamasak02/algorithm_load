"""方針
１：辞書順の改善が見込まれるものを先頭から順番に置き換える
２：辞書順の逆に後ろになるものについては後ろから入れ替える
"""


def main():
    smaller_indexes = []
    bigger_indexes = []
    result = []
    s = input()
    t = input()
    size = len(s)
    for i in range(size):
        if ord(s[i]) > ord(t[i]):
            smaller_indexes.append(i)
        elif ord(s[i]) < ord(t[i]):
            bigger_indexes.append(i)
    bigger_indexes.sort(reverse=True)
    chars = list(s)
    for index in smaller_indexes:
        chars[index] = t[index]
        result.append("".join(chars))
    for index in bigger_indexes:
        chars[index] = t[index]
        result.append("".join(chars))
    print(len(result))
    for word in result:
        print(word)
    return


if __name__ == "__main__":
    main()
