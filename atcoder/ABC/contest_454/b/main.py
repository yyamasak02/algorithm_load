def main():
    N, M = map(int, input().split())
    F = list(map(int, input().split()))
    origin_size = len(F)
    total_species = len(set(F))
    is_all_different_clothes = "Yes" if origin_size == total_species else "No"
    is_clothes_all_used = "Yes" if total_species == M else "No"
    print(is_all_different_clothes)
    print(is_clothes_all_used)
    return


if __name__ == "__main__":
    main()
