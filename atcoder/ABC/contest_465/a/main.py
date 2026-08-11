def main():
    A, B = map(int, input().split())
    result = "Yes" if float(A) > float(B) * (2 / 3) else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
