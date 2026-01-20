def main():
    n = int(input())
    s = input()
    odd_a_count = 0
    even_a_count = 0
    odd_progress = 1
    even_progress = 2
    for i in range(2 * n):
        if s[i] == "A":
            current = i + 1
            odd_a_count += abs(odd_progress - current)
            even_a_count += abs(even_progress - current)
            odd_progress += 2
            even_progress += 2
    print(min(odd_a_count, even_a_count))
    return


if __name__ == "__main__":
    main()
