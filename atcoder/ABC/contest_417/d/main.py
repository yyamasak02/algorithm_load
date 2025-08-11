if __name__ == "__main__":
    n: int = None
    p: int = None
    #    a: int = None
    b: int = None
    q: int = None
    x: int = None
    answers: list[list[int]] = []
    tensions: list[list[int]] = []

    n = int(input())
    for i in range(n):
        p, a, b = map(int, input().split())
        tensions.append([p, a, b])
    q = int(input())
    for i in range(q):
        x = int(input())
        answers.append([i, x, 0])
    answers.sort(key=lambda x: x[1])
    print(answers)
