def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    finally_array_sum = sorted([e * (N - i) for i, e in enumerate(A)], key=lambda x: -x)
    print(sum(finally_array_sum[K:]))
    return


if __name__ == "__main__":
    main()
