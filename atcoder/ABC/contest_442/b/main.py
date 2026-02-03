def main():
    is_running = False
    volume = 0
    q = int(input())
    for _ in range(q):
        a = int(input())
        if a == 1:
            volume += 1
        elif a == 2:
            volume = max(volume - 1, 0)
        else:
            is_running = not is_running

        if is_running and volume >= 3:
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
