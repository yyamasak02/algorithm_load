def main():
    x = list(input())
    a = list(map(int, x))
    a.sort(reverse=False)
    start_index = None
    for i in range(len(x)):
        if a[i] != 0:
            start_index = i
            break
    if start_index is not None:
        v = a.pop(start_index)
        a.insert(0, v)
    # print(start_index, v, a)
    print("".join(list(map(str, a))))
    return


if __name__ == "__main__":
    main()
