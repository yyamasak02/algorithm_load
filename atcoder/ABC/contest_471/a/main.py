def main():
    a, b = map(int, input().split())
    result = (
        "Nine" if a + b == 9 or a - b == 9 or a * b == 9 or a / b == 9.0 else "Nein"
    )
    print(result)
    return


if __name__ == "__main__":
    main()
