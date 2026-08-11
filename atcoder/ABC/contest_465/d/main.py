from collections import deque


def main():
    T = int(input())
    for _ in range(T):
        X, Y, K = map(int, input().split())
        q = deque()
        q.append((X, 0))
        visited = {X}
        while q:
            x, counter = q.popleft()
            print(x, counter)
            if x == Y:
                print(counter)
                break
            A, B = x // K, x * K
            if A not in visited:
                q.append((A, counter + 1))
                visited.add(A)
            if B not in visited:
                q.append((B, counter + 1))
                visited.add(B)
    return


if __name__ == "__main__":
    main()
