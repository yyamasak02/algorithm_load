def main():
    ll = list("HelloWorld")
    x = int(input())
    ll.pop(x - 1)
    print("".join(ll))
    return


if __name__ == "__main__":
    main()
