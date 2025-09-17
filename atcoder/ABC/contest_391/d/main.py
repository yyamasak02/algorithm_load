if __name__ == "__main__":
    n, w = map(int, input().split())
    blocks: list[tuple] = []
    block_count_per_col: list[int] = [0 for i in range(w + 1)]
    expired_at_steps: list[int] = [0 for i in range(n + 1)]
    block_belongs_step: list[int] = [0 for i in range(n + 1)]
    for i in range(n):
        query = tuple(map(int, input().split()))
        blocks.append((*query, i + 1))
    blocks.sort(key=lambda x: x[1])
    for query in blocks:
        block_count_per_col[query[0]] += 1
        block_belongs_step[query[2]] = block_count_per_col[query[0]]
        expired_at_steps[block_count_per_col[query[0]]] = max(
            expired_at_steps[block_count_per_col[query[0]]], query[1]
        )

    min_step: int = min(block_count_per_col[1::])
    q: int = int(input())
    # from pprint import pprint
    # pprint(block_belongs_step)
    # pprint(block_count_per_col)
    # pprint(expired_at_steps)
    # print(min_step)
    for _ in range(q):
        t, a = map(int, input().split())
        block_belongs = block_belongs_step[a]
        # print(f"[DEBUG] block belongs: {block_belongs}")
        if min_step < block_belongs:
            print("Yes")
            continue
        if t < expired_at_steps[block_belongs]:
            print("Yes")
        else:
            print("No")
