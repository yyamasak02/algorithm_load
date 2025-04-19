N, K = map(int, input().split())
S: str = input()
maru_count: int = S.count("o")
dot_count: int = S.count(".")
q_count: int = S.count("?")

print("maru_count:", maru_count)
print("dot_count:", dot_count)
print("q_count:", q_count)
